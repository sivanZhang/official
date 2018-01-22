#! -*- coding:utf-8 -*-
import pdb
import json
import random
import string
import os
from datetime import datetime
from django.shortcuts import redirect 
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
from area.models import Area

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

from django import forms

class DeptForm(forms.ModelForm): 
    class Meta:
        model = models.Dept
        fields = ('detail',)

class DeptView(View):
    """
    """

    @method_decorator(login_required)
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
        depts = models.Dept.objects.all()
     
        content['depts'] = depts
        content['mediaroot'] = settings.MEDIA_URL
        #form = DeptForm(instance=product)
        form = DeptForm()
        content['form'] = form
        if 'new' in request.GET:
            if request.user.is_anonymous(): 
                return redirect('users/login/?next=dept/list?new')

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
            deptid =  request.GET['detail']
            try:
                dept = models.Dept.objects.get(pk = deptid)
            except models.Dept.DoesNotExist:
                dept = dept[0]
            content['dept'] = dept
            if isMble:
                return render(request, 'dept/detail.html', content)
            else:
                return render(request, 'dept/detail.html', content)
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
        
        if 'name' in request.POST and 'storetype' in request.POST and \
           'phone' in request.POST and 'detail' in request.POST \
            and 'address' in request.POST  and 'area' in request.POST: 
            name = request.POST['name'].strip() 
            storetype = request.POST['storetype'].strip() 
            phone = request.POST['phone'].strip() 
            detail = request.POST['detail'].strip() 
            address = request.POST['address'].strip() 
            areaid = request.POST['area'].strip() 
            area = Area.objects.get(id = areaid)

            # 创建Block 
            dept = models.Dept.objects.create(
                user = user, 
                name = name ,
                dept_type = int(storetype) ,
                phone = phone ,
                detail = detail,
                area = area,
                address = address
            ) 
            result['id'] = dept.id
            result['status'] ='ok'
            result['msg'] = _('Saved completely!') 
        else:
            result['status'] ='error'
            result['msg'] ='Need parameter in POST'
        return self.httpjson(result)
    
    def put(self, request):
        """修改""" 
        # 修改时：deptid字段是必须的,title\url\pic\mark\status是可选字段
        user = request.user
        result = {}
        if 'deptid' in request.POST : 
            deptid = request.POST['deptid'].strip() 

            # 创建Block 
            block = models.Dept.objects.get(pk = deptid)
            
            if  'title' in request.POST  :
                title = request.POST['title'].strip()
                dept.title = title
            
            if 'pic' in request.FILES:
                pic = request.FILES['pic'] 
                pic_url = handle_uploaded_file(pic, user.id)
                dept.pic = pic_url

            if  'url' in request.POST  :
                url = request.POST['url'].strip()
                dept.url = url
            
            if 'mark' in request.POST:
                mark = request.POST['mark'].strip() 
                if mark:
                    dept.mark = mark
            
            if 'status' in request.POST:
                status = request.POST['status'].strip()   
                dept.status = int(status)
            
            dept.save()
            result['id'] = dept.id
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
            deptid = request.POST['id'].strip() 
            try:
                dept = models.Dept.objects.get(pk = deptid)
                dept.delete()
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

