# -*- coding:utf-8 -*-
import json
from datetime import datetime
import pdb
from django.shortcuts import render
from django.http import HttpResponse
from pay.controller import MainController
from pay.PayToolUtil import PayToolUtil
from book.apis import pay_book, sendsms
from django.urls import reverse
from django.shortcuts import redirect

def weixin(request):
    """
    微信支付查询API
    """
    content = {}
    content['status'] = 'error'
    
    billno = request.GET.get('billno')
    if billno is None:
        content['msg'] = '请在GET中提供billno订单号.'
        return HttpResponse(json.dumps(content), content_type="application/json")

    content = checkbill(billno)
    if content['status'] == 'ok':
        
        if 'book' in content: 
            content['book']  = content['book'].id
            content['status'] = 'go' # 跳转
             
    return HttpResponse(json.dumps(content), content_type="application/json")

def checkbill(billno):
    """
    检查bill订单状态
    """
    paycheck = PayToolUtil()
    weixin_returned = paycheck.getQueryUrl(billno)
    weixin_returned = weixin_returned['xml']

    return_code = weixin_returned['return_code']
    result_code = weixin_returned['result_code']
    
    content = {}
    content['status'] = 'error'
    if return_code == PayToolUtil._SUCCESS and result_code == PayToolUtil._SUCCESS :
        """
        trade_state:
        SUCCESS—支付成功
        REFUND—转入退款
        NOTPAY—未支付
        CLOSED—已关闭
        REVOKED—已撤销（刷卡支付）
        USERPAYING--用户支付中
        PAYERROR--支付失败(其他原因，如银行返回失败)
        支付状态机请见下单API页面
        """
        trade_state = weixin_returned['trade_state']
        
        if  trade_state == PayToolUtil._SUCCESS : 
            # 订单支付成功，更新bill
            transaction_id = weixin_returned['transaction_id']
            total_fee = int(weixin_returned['total_fee']) / 100
            order_id = weixin_returned['out_trade_no']  
            send_pay_date = weixin_returned['time_end']
            send_pay_date = datetime.strptime(send_pay_date, '%Y%m%d%H%M%S')
        
            pay_way = 'weixin'
            result = {}
            result = pay_book(order_id, pay_way, total_fee, transaction_id, send_pay_date)
            if result['status'] == 'ok':
                #返回成功页面 
                content['status'] = 'ok'
                content['book'] = result['book']  
            else:
                content['msg'] = result['msg']
        else:
            # 未成功
            """
            SUCCESS—支付成功

            REFUND—转入退款

            NOTPAY—未支付

            CLOSED—已关闭

            REVOKED—已撤销（刷卡支付）

            USERPAYING--用户支付中

            PAYERROR--支付失败(其他原因，如银行返回失败)
            """
            if trade_state == 'REFUND':
                 content['msg'] = '转入退款'
            elif trade_state == 'NOTPAY':
                content['status'] = 'ok'
                content['msg'] = '未支付'
            elif trade_state == 'CLOSED':
                content['msg'] = '已关闭'
            elif trade_state == 'REVOKED':
                content['msg'] = '已撤销（刷卡支付）'
            elif trade_state == 'USERPAYING':
                content['msg'] = '用户支付中'
            else:
                content['msg'] = '支付失败(其他原因，如银行返回失败)'
        
    return content