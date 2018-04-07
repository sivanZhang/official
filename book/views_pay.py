import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from alipay import AliPay
import os
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from common.e_mail import EmailEx

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()
import pdb
from book.apis import pay_book

def alipay(order_id, total_amount, subject):
    #request.POST.get("order_id")
    # 创建用于进行支付宝支付的工具对象
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_path=settings.PRIVATE_KEY,
        alipay_public_key_path=settings.ALI_PUBLIC_KEY,

        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False  配合沙箱模式使用
    )

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no = order_id,
        total_amount = str(total_amount),  # 将Decimal类型转换为字符串交给支付宝
        subject = subject,
        return_url = settings.ALIPAY_RETURN_URL,
        notify_url = settings.ALIPAY_NOTIFY_URL  # 可选, 不填则使用默认notify url
    )

    # 让用户进行支付的支付宝页面网址
    url = settings.ALIPAY_URL + "?" + order_string
    return url
    # return redirect(url)
     
    #return JsonResponse({"code": 0, "message": "请求支付成功", "url": url})

def alipay_notify(request):
    """

    """
    
    return HttpResponse("get from alipay")

def alipay_check_pay(request):
    # 创建用于进行支付宝支付的工具对象
     
    order_id = request.GET['out_trade_no']
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_path=settings.PRIVATE_KEY,
        alipay_public_key_path=settings.ALI_PUBLIC_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA2,官方推荐，配置公钥的时候能看到
        debug=False  # 默认False  配合沙箱模式使用
    )

    while True:
        # 调用alipay工具查询支付结果
        resp = alipay.api_alipay_trade_query(order_id)  # resp是一个字典
        # 判断支付结果
        code = resp.get("code")  # 支付宝接口调用成功或者错误的标志
        trade_status = resp.get("trade_status")  # 用户支付的情况
        
        # {'code': '10000', 'msg': 'Success', 'buyer_logon_id': 'fet***@sandbox.com', 
        # 'buyer_pay_amount': '0.00', 'buyer_user_id': '2088102175947174', 
        # 'buyer_user_type': 'PRIVATE', 'invoice_amount': '0.00', 
        # 'out_trade_no': '3232423111443234ASU', 'point_amount': '0.00', 
        # 'receipt_amount': '0.00', 'send_pay_date': '2018-03-29 23:12:40', 
        # 'total_amount': '0.01', 'trade_no': '2018032921001004170200926730', 
        # 'trade_status': 'TRADE_SUCCESS'}

        
        if code == "10000" and trade_status == "TRADE_SUCCESS":
            # 表示用户支付成功
            # 返回前端json，通知支付成功
            isMble  = dmb.process_request(request)
            trade_no = resp.get("trade_no")
            total_amount = resp.get("total_amount")
            send_pay_date = resp.get("send_pay_date")
            pay_way = 'zhifubao'
            
            result = pay_book(order_id, pay_way, total_amount, trade_no, send_pay_date) 
            if result['status'] == 'ok':
                #返回成功页面 
                content = {}
                book = result['book'] 
                content['billno'] = book.billno
                content['book'] = book 
        
                emailex = EmailEx()
                emailcontent = """
                您好！
                <br/>
                感谢您预约最新款ASU Watch， 我们将在到货后第一时间通过短信、邮件等方式联系您，您可输入预约码xxx直接抵扣200元。
                <br/>
                请妥善保留此邮件！
                """
                smscontent = """您已成功预约，到货后第一时间会发短信联系您，您可输入预约码xxx直接抵扣200元。请妥善保留此短信。"""
                emailcontent = emailcontent.replace('xxx', book.billno)
                smscontent = smscontent.replace('xxx', book.billno)
                #emailex.send_text_email("一数科技预约支付", emailcontent, book.email)
                req = requests.get(settings.SMS_API.format(book.phone, smscontent) )
               
                if isMble:
                    return render(request, 'book/success.html', content)
                else:
                    return render(request, 'book/success.html', content)
            else:
                return HttpResponse("订单异常...")
            
            #return JsonResponse({"code": 0, "message": "支付成功"})
             
        elif code == "40004" or (code == "10000" and trade_status == "WAIT_BUYER_PAY"):
            # 表示支付宝接口调用暂时失败，（支付宝的支付订单还未生成） 后者 等待用户支付
            # 继续查询
            print(code)
            print(trade_status)
            continue
        else:
            # 支付失败
            # 返回支付失败的通知
            return JsonResponse({"code": 1, "message": "支付失败"})