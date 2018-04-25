# -*- coding:utf-8 -*-
#Author：叶国坚


import os
import datetime
import time 
import base64
import json
from datetime import datetime
from decimal import Decimal
import socket
import qrcode
from io import BytesIO
from pay.PayToolUtil import *
from django.http import HttpResponse
from django.conf import settings

class MainController(object):
    #获取微信二维码
    def getWeChatQRCode(self, **kwargs):
        order_id = kwargs.get('order_id') #获取客户端生成的订单号
        goodsName = kwargs.get('goodsName') #获取商品信息
        goodsPrice = int(float(kwargs.get('goodsPrice')) * 100) #获取价格，单位是分，需要是整数
        
        toolUtil = PayToolUtil()
        code_url=toolUtil.getPayUrl(order_id,goodsName,goodsPrice) #调用统一下单方法，获得支付订单的url链接
        
        if code_url:
            res_info = code_url
        # 如果成功获得支付链接，则写入一条订单记录
        #todo：自己的后台逻辑
        else:
            res_info = "二维码失效" #获取url失败，则二维码信息为失效
        
        #根据res_info生成二维码，使用qrcode模块
        qr = qrcode.QRCode(
                           version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_H,
                           box_size=10,
                           border=1
                           )
        qr.add_data(res_info) #二维码所含信息
        img = qr.make_image() #生成二维码图片
        paydir = os.path.join(settings.MEDIA_ROOT, 'pay')
        if not os.path.isdir(paydir):
            os.makedirs(paydir)
        img.save(os.path.join(paydir,  order_id+'weixinqr.png'))
        """
        byte_io = BytesIO()
        img.save(byte_io, 'PNG') #存入字节流
        byte_io.seek(0)
        return HttpResponse(byte_io, content_type='image/png') #把字节流返回给客户端，解析得到二维码
        """


    #微信支付回调
    def weChatQRCodeNotify(self, request, *args,**kwargs):
        order_result_xml = http.request.httprequest.stream.read() #从请求流提取数据
        doc = xmltodict.parse(order_result_xml) #解析得到的xml字符串，转为dict
        out_trade_no = doc['xml']['out_trade_no'] #提取返回数据中的订单号
        #todo：提取签名、支付金额等，验证签名是否正确、金额是否正确
        #思路：在前面获取二维码时，生成了一条订单记录，订单应该保存下订单号、签名、金额等信息。在这里，根据回传的订单号查询数据库，得到对应的签名、金额进行验证即可
        #最后，别忘了应答微信支付平台，防止重复发送数据
        return '''
            <xml>
            <return_code><![CDATA[SUCCESS]]></return_code>
            <return_msg><![CDATA[OK]]></return_msg>
            </xml>
            '''
    
    # 支付结果轮询:客户端根据订单号轮询订单模型记录，状态为 支付成功 
    # 则返回出货信号，客户端验证信号为出货，则停止轮询，并控制出货
    def weChatQRCodeHadPay(self, **kwargs):
        order_id = kwargs.get('order_id') #获取订单号
        #todo：根据订单号查询对应的订单记录状态，返回支付结果



