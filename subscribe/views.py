#! -*- coding:utf-8 -*-
import pdb
import json  
import time
from datetime import datetime
from django.shortcuts import redirect 
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import Http404, QueryDict
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.detail import DetailView
from django.db.utils import IntegrityError
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from django.utils.translation import ugettext as _
from django.utils.decorators import method_decorator
from subscribe import models   
 
def send(request):
    msg = {}
    if 'phone' in request.POST and 'deptid' in request.POST:
        deptid = request.POST['deptid']
        phone = request.POST['phone']
        dept = models.Subscribe.objects.get(pk = deptid)
        int_time = int(time.time())
        if 'time' in request.session:
            old_int_time = request.session['time']
            request.session['time'] = int_time
            if int_time - old_int_time < 60:# 60秒，频率太高
                msg['status'] = 'error'
                msg['msg'] = u'操作频率太快...'
            else: 
                content = "【"+settings.PROJECTNAME+"】" + dept.name + ':'+ dept.address + "电话：" + dept.phone
                req = requests.get(settings.SMS_API.format(phone,content)) 
                msg['status'] = 'ok'
                msg['msg'] = u'已发送...'
        else:
            old_int_time = 0
            content = "【"+settings.PROJECTNAME+"】" + dept.name + ':'+ dept.address + "电话：" + dept.phone
            req = requests.get(settings.SMS_API.format(phone,content))   
            request.session['time'] = int_time
            msg['status'] = 'ok'
            msg['msg'] = u'已发送...'
    else:
        msg['status'] = 'error'
        msg['msg'] = u'方法错误...'
    return HttpResponse(json.dumps(msg), content_type="application/json")

class SubscribeView(View):
    """
    订阅
    """  
    def get(self, request): 
        content = {}  
        return render(request, 'dept/list.html', content)
       
    @method_decorator(csrf_exempt)
    def post(self,request ): 
        if 'method' in request.POST:
            method = request.POST['method'].lower() 
            if method == 'create': # 创建
                return self.create(request) 
            elif method == 'delete': # 删除
                return self.delete(request)  
        else:
            self.create(request)
            return self.get(request)
 
    def create(self, request):
        """创建""" 
        user = request.user
        result = {}  
        if 'name' in request.POST and 'email' in request.POST : 
            name = request.POST['name'].strip() 
            email = request.POST['email'].strip()  
            try:
                sub_instance = models.Subscribe.objects.create( 
                    name = name ,
                    email = email
                ) 
                result['id'] = sub_instance.id
                result['status'] ='ok'
                result['msg'] = _('Saved completely!')
            except IntegrityError:
                pass
             
        else:
            result['status'] ='error'
            result['msg'] ='Need parameter in POST'
        return self.httpjson(result)
    
     
    def delete(self, request):
        user = request.user
        result = {}
        if 'id' in request.POST : 
            subid = request.POST['id'].strip() 
            try:
                sub_instance = models.Subscribe.objects.get(pk = subid)
                sub_instance.delete()
                result['status'] ='ok'
                result['msg'] = _('Done')
            except models.Subscribe.DoesNotExist:
                result['status'] ='error'
                result['msg'] = _('Not found')
        else:
            result['status'] ='error'
            result['msg'] = 'Need title  in POST'
        
        return self.httpjson(result)

    def httpjson(self, result):
        return HttpResponse(json.dumps(result), content_type="application/json")

