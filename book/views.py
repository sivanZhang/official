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
from django.shortcuts import redirect 

from book import models
from book.apis import pay_book
from book.views_pay import alipay

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

class BookView(View):
 
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
        books = models.AdaptorBook.objects.all()
     
        content['books'] = books
        content['number'] = len(books)
        if 'new' in request.GET:
            if isMble:
                return render(request, 'book/m_blocknew.html', content)
            else:
                return render(request, 'book/blocknew.html', content)

        if 'test' in request.GET:
            if isMble:
                return render(request, 'book/test.html', content)
            else:
                return render(request, 'book/test.html', content)
        if 'detail' in request.GET:
            if isMble:
                return render(request, 'book/m_detail.html', content)
            else:
                return render(request, 'book/m_detail.html', content)
        else:
            if isMble:
                return render(request, 'book/buy.html', content)
            else:
                return render(request, 'book/buy.html', content)

    
    @method_decorator(csrf_exempt)
    def post(self,request ): 
        if 'method' in request.POST:
            method = request.POST['method'].lower()
            if method == 'put':# 修改
                self.put(request)
                return   self.get(request)
            elif method == 'create': # 预约
                return self.create(request) 
            elif method == 'delete': # 删除
                return self.delete(request) 
        else:
            return self.create(request)
            

    def create(self, request):
        """预约""" 
        # 预约时  
        result = {} 
        isMble  = dmb.process_request(request)
        content = {}  
        if 'name' in request.POST and  'phone' in request.POST and  'email' in request.POST \
            and  'address' in request.POST: 
            name = request.POST['name'].strip() 
            phone = request.POST['phone'].strip()
            address = request.POST['address'].strip()
            email = request.POST['email'].strip()
            code    = ''.join(random.choice(string.digits) for i in range(4))
            billno = datetime.now().strftime('%Y%m%d%H%M%S')+str(code) 
            
            if name == '' or phone == '': 
                books = models.AdaptorBook.objects.all()
                content['number'] = len(books)
                content['error'] = 'error' 
                content['msg'] = _('Name  and Phone cannot be empty!') 

                content['name'] = 'name' 
                content['phone'] = 'phone' 
                content['email'] = 'email' 
                content['address'] = 'address' 

                if isMble:
                    return render(request, 'book/buy.html', content)
                else:
                    return render(request, 'book/buy.html', content)
            else:
                # 预约 
                book = models.AdaptorBook.objects.create(name=name, phone=phone, \
                            billno=billno, address=address )
                if email:
                    book.email = email
                book.save()

                # 开始支付
                book_money  = 0.01
                subject = "一数预约支付"
                return redirect (alipay(billno, book_money, subject))
                
                content['billno'] = book.billno
                result['status'] ='ok'
                result['msg'] = _('Saved completely!') 
                if isMble:
                    return render(request, 'book/success.html', content)
                else:
                    return render(request, 'book/success.html', content)
        else:
            content['status'] ='error'
            content['msg'] ='Need title  in POST' 
            if isMble:
                return render(request, 'book/buy.html', content)
            else:
                return render(request, 'book/buy.html', content)
         
    
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


 