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

from dept import models 

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

from django import forms

class DeptForm(forms.ModelForm): 
    class Meta:
        model = models.Dept
        fields = ('detail',)

class DeptView(View):
    @method_decorator(login_required)
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
        blocks = models.Dept.objects.all()
     
        content['blocks'] = blocks
        content['mediaroot'] = settings.MEDIA_URL
        #form = DeptForm(instance=product)
        form = DeptForm()
        content['form'] = form
        if 'new' in request.GET:
            if isMble:
                return render(request, 'dept/new.html', content)
            else:
                return render(request, 'dept/new.html', content)

        if 'test' in request.GET:
            if isMble:
                return render(request, 'dept/test.html', content)
            else:
                return render(request, 'dept/test.html', content)
        if 'detail' in request.GET:
            if isMble:
                return render(request, 'dept/m_detail.html', content)
            else:
                return render(request, 'dept/m_detail.html', content)
        else:
            if isMble:
                return render(request, 'dept/list.html', content)
            else:
                return render(request, 'dept/list.html', content)

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def post(self,request ): 
        if 'method' in request.POST:
            method = request.POST['method'].lower()
            if method == 'put':# 修改
                self.put(request)
                return   self.get(request)
            elif method == 'create': # 创建
                return self.create(request) 
            elif method == 'delete': # 删除
                return self.delete(request) 
        else:
            self.create(request)
            return self.get(request)

    def create(self, request):
        """创建""" 
        # 创建时：title字段是必须的,\url\pic\mark\status是可选字段
        user = request.user
        result = {} 
        
        if 'title' in request.POST : 
            title = request.POST['title'].strip() 

            # 创建Block 
            block = models.Dept.objects.create(user=user, title=title )
            
            if 'url' in request.POST  :
                url = request.POST['url'].strip()
                block.url = url
  
            if 'pic' in request.FILES:
                pic = request.FILES['pic'] 
                pic_url = handle_uploaded_file(pic, user.id)
                block.pic = pic_url
            
            if 'mark' in request.POST:
                mark = request.POST['mark'].strip() 
                if mark:
                    block.mark = mark
            
            if 'status' in request.POST:
                status = request.POST['status'].strip() 
                if int(status):
                    block.status = int(status)
    
            block.save()
            result['id'] = block.id
            result['status'] ='ok'
            result['msg'] = _('Saved completely!') 
        else:
            result['status'] ='error'
            result['msg'] ='Need title  in POST'
        return self.httpjson(result)
    
    def put(self, request):
        """修改""" 
        # 修改时：blockid字段是必须的,title\url\pic\mark\status是可选字段
        user = request.user
        result = {}
        if 'blockid' in request.POST : 
            blockid = request.POST['blockid'].strip() 

            # 创建Block 
            block = models.Dept.objects.get(pk = blockid)
            
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
                block = models.Dept.objects.get(pk = blockid)
                block.delete()
                result['status'] ='ok'
                result['msg'] = _('Done')
            except models.Dept.DoesNotExist:
                result['status'] ='error'
                result['msg'] = _('Not found')
        else:
            result['status'] ='error'
            result['msg'] = 'Need title  in POST'
        
        return self.httpjson(result)

    def httpjson(self, result):
        return HttpResponse(json.dumps(result), content_type="application/json")

