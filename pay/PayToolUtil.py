# -*- coding:utf-8 -*-
#Author： 

import pdb
import socket
import string
import time
import random
import requests
import string
import json
import hashlib
import xmltodict
import sys
import urllib
#import urllib2
import re

from django.conf import settings

class PayToolUtil(object):

    # ========支付相关配置信息===========
    _APP_ID = settings.WEIXIN['app_id'];  # 公众账号appid
    _MCH_ID = settings.WEIXIN['mch_id'];  # 商户号
    _API_KEY = settings.WEIXIN['app_seckey'];  # key设置路径：微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置

    # 有关url
    _host_name = socket.gethostname()
    _ip_address = socket.gethostbyname(_host_name)
    _CREATE_IP = _ip_address  # 发起支付的ip
    
    _UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"
    _QUERY_URL = "https://api.mch.weixin.qq.com/pay/orderquery"
    _NOTIFY_URL = "47.95.239.228:8000/pay/weixin/"#"your Ip：端口／处理方法路径";  # 微信支付结果回调的处理方法
    _SUCCESS = 'SUCCESS'

    def getPayUrl(self,orderid,goodsName,goodsPrice,**kwargs):
        '''
        向微信支付端发出请求，获取url
        '''
        
        appid = self._APP_ID
        mch_id = self._MCH_ID
        key = self._API_KEY
        nonce_str = str(int(round(time.time() * 1000)))+str(random.randint(1,999))+" ".join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 5)).replace(" ","") #生成随机字符串
        spbill_create_ip = self._CREATE_IP
        notify_url = self._NOTIFY_URL
        trade_type = "NATIVE"

        params = {}
        params['appid'] = appid
        params['mch_id'] = mch_id
        params['nonce_str'] = nonce_str
        params['out_trade_no'] = orderid#.encode('utf-8')    #客户端生成并传过来，参数必须用utf8编码，否则报错
        params['total_fee'] = goodsPrice   #单位是分，必须是整数
        params['spbill_create_ip'] = spbill_create_ip
        params['notify_url'] = notify_url 
        params['body'] = goodsName.encode('utf-8')   #中文必须用utf-8编码，否则xml格式错误
        params['trade_type'] = trade_type

        #生成签名
        ret = []
        for k in sorted(params.keys()):
            if (k != 'sign') and (k != '') and (params[k] is not None):
                ret.append('%s=%s' % (k, params[k]))
        params_str = '&'.join(ret)
        params_str = '%(params_str)s&key=%(partner_key)s'%{'params_str': params_str, 'partner_key': key}
        #reload(sys)
        #sys.setdefaultencoding('utf8')
        params_str = hashlib.md5(params_str.encode('utf-8')).hexdigest()
        sign = params_str.upper()
        params['sign'] = sign


        #拼接参数的xml字符串
        request_xml_str = '<xml>'
        for key, value in params.items():
            if isinstance(value, str):
                request_xml_str = '%s<%s><![CDATA[%s]]></%s>' % (request_xml_str, key, value, key, )
            else:
                request_xml_str = '%s<%s>%s</%s>' % (request_xml_str, key, value, key, )
        request_xml_str = '%s</xml>' % request_xml_str

        #向微信支付发出请求，并提取回传数据
        #res = urllib2.Request(self._UFDODER_URL, data=request_xml_str)
        #res_data = urllib2.urlopen(res)
        res_data = requests.post(self._UFDODER_URL, data=request_xml_str)  
        res_read = res_data.content
        doc = xmltodict.parse(res_read)
        return_code = doc['xml']['return_code']
        if return_code=="SUCCESS":
            result_code = doc['xml']['result_code']
            if result_code=="SUCCESS":
                code_url = doc['xml']['code_url']
                return code_url
            else:
                err_des = doc['xml']['err_code_des']
                print ("errdes==========="+err_des)
        else:
            fail_des = doc['xml']['return_msg']
            print ("fail des============="+fail_des)
    
    def getQueryUrl(self,orderid):
        '''
        向微信支付查询接口，获取url
        1232137218973298173
        参考：
        https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_2
        '''
        
        appid = self._APP_ID
        mch_id = self._MCH_ID
        key = self._API_KEY
        nonce_str = str(int(round(time.time() * 1000)))+str(random.randint(1,999))+" ".join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 5)).replace(" ","") #生成随机字符串
  
        params = {}
        params['appid'] = appid
        params['mch_id'] = mch_id
        params['nonce_str'] = nonce_str
        params['out_trade_no'] = orderid #.encode('utf-8')    #客户端生成并传过来，参数必须用utf8编码，否则报错
          
        #生成签名
        ret = []
        for k in sorted(params.keys()):
            if (k != 'sign') and (k != '') and (params[k] is not None):
                ret.append('%s=%s' % (k, params[k]))
        params_str = '&'.join(ret)
        params_str = '%(params_str)s&key=%(partner_key)s'%{'params_str': params_str, 'partner_key': key}
        #reload(sys)
        #sys.setdefaultencoding('utf8')
        params_str = hashlib.md5(params_str.encode('utf-8')).hexdigest()
        sign = params_str.upper()
        params['sign'] = sign
 
        #拼接参数的xml字符串
        request_xml_str = '<xml>'
        for key, value in params.items():
            if isinstance(value, str):
                request_xml_str = '%s<%s><![CDATA[%s]]></%s>' % (request_xml_str, key, value, key, )
            else:
                request_xml_str = '%s<%s>%s</%s>' % (request_xml_str, key, value, key, )
        request_xml_str = '%s</xml>' % request_xml_str

        #向微信支付发出查询请求，并提取回传数据 
        res_data = requests.post(self._QUERY_URL, data=request_xml_str)
     
        res_read = res_data.content
        doc = xmltodict.parse(res_read)
        print(doc)
        return doc
        
        
        return_code = doc['xml']['return_code']
        if return_code=="SUCCESS":
            result_code = doc['xml']['result_code']
            if result_code=="SUCCESS":
                code_url = doc['xml']['code_url']
                return code_url
            else:
                err_des = doc['xml']['err_code_des']
                print ("errdes==========="+err_des)
        else:
            fail_des = doc['xml']['return_msg']
            print ("fail des============="+fail_des)















