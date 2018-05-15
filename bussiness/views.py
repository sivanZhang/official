#! -*- coding:utf-8 -*-
import pdb
import json
import random
import string
import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import Http404, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.utils.translation import ugettext as _
from common.e_mail import EmailEx
from book import models
 

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

class BussinessView(View): 
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
         
        if 'new' in request.GET:
            if isMble:
                return render(request, 'bussiness/m_blocknew.html', content)
            else:
                return render(request, 'bussiness/blocknew.html', content)

        if 'test' in request.GET:
            if isMble:
                return render(request, 'bussiness/test.html', content)
            else:
                return render(request, 'bussiness/test.html', content)
        if 'detail' in request.GET:
            if isMble:
                return render(request, 'bussiness/m_detail.html', content)
            else:
                return render(request, 'bussiness/m_detail.html', content)
        else:
            if isMble:
                return render(request, 'bussiness/new.html', content)
            else:
                return render(request, 'bussiness/new.html', content)

    
    @method_decorator(csrf_exempt)
    def post(self,request ): 
        if 'method' in request.POST:
            method = request.POST['method'].lower()
            if method == 'put':# 修改
                self.put(request)
                return   self.get(request)
            elif method == 'create': # 申请经销商
                return self.create(request) 
            elif method == 'delete': # 删除
                return self.delete(request)  
        else:
            return self.create(request) 

    def create(self, request):
        """申请经销商""" 
         
        user = request.user
        result = {} 
        isMble  = dmb.process_request(request)
        
        if 'trade_name' in request.POST and  'registered_name' in request.POST  and \
        'registered_adress' in request.POST and  'bill_adress' in request.POST   and \
        'receiving_adress' in request.POST and  'official_url' in request.POST    and \
        'surname' in request.POST and  'personal_name' in request.POST   and \
        'position' in request.POST and  'phone_number' in request.POST   and \
        'telautogram' in request.POST and  'email' in request.POST  : 

            trade_name = request.POST['trade_name'].strip() 
            registered_name = request.POST['registered_name'].strip() 
            registered_adress = request.POST['registered_adress'].strip() 
            bill_adress = request.POST['bill_adress'].strip() 
            receiving_adress = request.POST['receiving_adress'].strip() 

            official_url = request.POST['official_url'].strip() 
            surname = request.POST['surname'].strip() 

            personal_name = request.POST['personal_name'].strip() 
            position = request.POST['position'].strip() 
            phone_number = request.POST['phone_number'].strip() 
            telautogram = request.POST['telautogram'].strip() 
            email = request.POST['email'].strip()  
 
            stor_url = ''
            if 'stor_url' in request.POST  :
                stor_url = request.POST['stor_url'].strip()
                 
  
            other_url = ''
            if 'other_url' in request.POST  :
                other_url = request.POST['other_url'].strip()

            emailex = EmailEx()
            emailcontent = """
            您好！
            <br/>
            <strong>申请企业基本信息</strong>
            <br/>
            公司贸易名称: trade_name
            <br/>
            公司注册名称: registered_name
            <br/>
            <strong>申请企业基本信息</strong>
            <br/>
            注册地址: registered_adress
            <br/>
            账单地址: bill_adress
            <br/>
            收货地址: receiving_adress
            <br/>
            <strong>企业网站信息</strong>
            <br/>
            企业网站地址: official_url
            <br/>
            电商网址: stor_url
            <br/>
            其他: other_url
            <br/>
            <strong>企业网站信息</strong>
            <br/>
            姓: surname
            名: personal_name
            <br/>
            职位: position
            <br/>
            电话: phone_number
            <br/>
            传真: telautogram
            <br/>
            电子邮件: email
            <br/>
            <br/>
            <strong>一数科技</strong>
            
            """
            emailcontent = emailcontent.replace('trade_name', trade_name)
            emailcontent = emailcontent.replace('registered_name', registered_name)
            emailcontent = emailcontent.replace('registered_adress', registered_adress)
            emailcontent = emailcontent.replace('bill_adress', bill_adress)
            emailcontent = emailcontent.replace('receiving_adress', receiving_adress)

            emailcontent = emailcontent.replace('official_url', official_url)
            emailcontent = emailcontent.replace('stor_url', stor_url)
            emailcontent = emailcontent.replace('other_url', other_url)
            emailcontent = emailcontent.replace('surname', surname)
            emailcontent = emailcontent.replace('personal_name', personal_name)

            emailcontent = emailcontent.replace('position', position)
            emailcontent = emailcontent.replace('phone_number', phone_number)
            emailcontent = emailcontent.replace('telautogram', telautogram)
            emailcontent = emailcontent.replace('email', email)
             
            emailex.send_text_email("新的经销商申请", emailcontent, 'bjbd001@a-su.com.cn')
             
            if isMble:
                return render(request, 'bussiness/m_success.html', {})
            else:
                return render(request, 'bussiness/success.html', {})
        else:
            content['msg'] = "申请信息不完整"
            if isMble:
                return render(request, 'bussiness/new.html', content)
            else:
                return render(request, 'bussiness/new.html', content)
    
    def put(self, request):
        """修改""" 
        # 修改时：blockid字段是必须的,title\url\pic\mark\status是可选字段
        user = request.user
        result = {}
        if 'blockid' in request.POST : 
            blockid = request.POST['blockid'].strip() 

            # 预约Block 
            block = models.AdaptorBook.objects.get(pk = blockid)
            
            if  'title' in request.POST  :
                title = request.POST['title'].strip()
                block.title = title
            
            if 'pic' in request.FILES:
                pic = request.FILES['pic'] 
                pic_url = handle_uploaded_file(pic, user.id)
                block.pic = pic_url

            if  'url' in request.POST  :
                url = request.POST['url'].strip()
                block.url = url
            
            if 'mark' in request.POST:
                mark = request.POST['mark'].strip() 
                if mark:
                    block.mark = mark
            
            if 'status' in request.POST:
                status = request.POST['status'].strip()   
                block.status = int(status)
            
            block.save()
            result['id'] = block.id
            result['status'] ='ok'
            result['msg'] = _('Saved completely!') 
        else:
            result['status'] ='error'
            result['msg'] ='Need title  in POST'
        return self.httpjson(result)

    def delete(self, request):
        user = request.user
        result = {}
        if 'id' in request.POST : 
            blockid = request.POST['id'].strip() 
            try:
                block = models.AdaptorBook.objects.get(pk = blockid)
                block.delete()
                result['status'] ='ok'
                result['msg'] = _('Done')
            except models.AdaptorBook.DoesNotExist:
                result['status'] ='error'
                result['msg'] = _('Not found')
        else:
            result['status'] ='error'
            result['msg'] = 'Need title  in POST'
        
        return self.httpjson(result)

    def httpjson(self, result):
        return HttpResponse(json.dumps(result), content_type="application/json")


 