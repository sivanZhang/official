#! -*- coding:utf-8 -*-
import pdb
import json
import random
import string
import os
import time
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
from django.db.models import Q
import requests
from dept import models 
from area.models import Area
from area.views import get_provice_list, get_city_list, get_county_list, byte2json
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

from django import forms

class DeptForm(forms.ModelForm): 
    class Meta:
        model = models.Dept
        fields = ('detail',)

def send(request):
    msg = {}
    if 'phone' in request.POST and 'deptid' in request.POST:
        deptid = request.POST['deptid']
        phone = request.POST['phone']
        dept = models.Dept.objects.get(pk = deptid)
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

class DeptView(View):
    """
    """

    #@method_decorator(login_required)
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
        depts = models.Dept.objects.all() 
        content['depts'] = depts
        content['storepage'] = True
        content['mediaroot'] = settings.MEDIA_URL
        #form = DeptForm(instance=product)
        
        if 'new' in request.GET:
            form = DeptForm()
            content['form'] = form
            depts = depts.filter(store_type = 0)
            content['depts'] = depts
            if request.user.is_anonymous(): 
                return redirect('users/login/?next=dept/list?new')

            if isMble:
                return render(request, 'dept/new.html', content)
            else:
                return render(request, 'dept/new.html', content)
        if 'newservice' in request.GET:
            form = DeptForm()
            content['form'] = form
            depts = depts.filter(store_type = 1)
            content['depts'] = depts
            if request.user.is_anonymous(): 
                return redirect('users/login/?next=dept/list?new')

            if isMble:
                return render(request, 'dept/new_service.html', content)
            else:
                return render(request, 'dept/new_service.html', content)
        if 'servicesearch' in request.GET:
            depts = depts.filter(store_type = 1)
            provices = get_provice_list(request)
            provices_json = byte2json(provices.content) 
            content['provices'] = provices_json 
            
            if 'provice' in request.GET: 
                provice = request.GET['provice']
                try:
                    provice_instance = Area.objects.get(id=provice) 
                    cities = Area.objects.filter(parent_id=provice_instance.id) 
                    content['cities'] = cities 
                    cities_id = []
                    for cityitem in cities:
                        cities_id.append(cityitem.id)
                    if provice == '110100':
                        depts = depts.filter(area__in = cities_id)
                    else:
                        depts = depts.filter(area__parent_id__in = cities_id)
                    content['provicearea'] = provice_instance 
                except Area.DoesNotExist:
                    pass
            else:
                pass 
            content['depts'] = depts
            #areas = [area]
            if isMble:
                return render(request, 'dept/servicelist.html', content)
            else:
                return render(request, 'dept/servicelist.html', content)
        if 'detail' in request.GET:
            deptid =  request.GET['detail']
            try:
                dept = models.Dept.objects.get(pk = deptid)
                area = Area.objects.get(id = dept.area.parent_id)
                content['area'] = area
            except models.Dept.DoesNotExist:
                dept = depts[0]
            content['dept'] = dept
            if isMble:
                return render(request, 'dept/detail.html', content)
            else:
                return render(request, 'dept/detail.html', content)
        else:
            # 获取北京的门店：110100
            if 'provice' in request.GET and 'city' in request.GET and 'county' in request.GET:
                provice = request.GET['provice']
                city = request.GET['city']
                county = request.GET['county']
                storetype = request.GET.get('storetype')
                content['storetype'] = storetype

                try:
                    # 根据区县搜索
                    county_instance = Area.objects.get(id=county) 
                    provice_instance = Area.objects.get(id=provice)
                    city_instance = Area.objects.get(id=county_instance.parent_id)
                    
                    cities = Area.objects.filter(parent_id=city_instance.parent_id)
                    counties = Area.objects.filter(parent_id=city_instance.id)
              
                    content['cities'] = cities
                    content['counties'] = counties 

                    content['county'] = county_instance
                    content['city'] = city_instance # 市 
                    content['provicearea'] = provice_instance
                    if storetype == '0':
                        depts = depts.filter(area = county_instance)
                    else:
                        depts = depts.filter(area = county_instance, dept_type=storetype)

                except Area.DoesNotExist: 
                    #　根据市搜索
                    try:
                        city_instance = Area.objects.get(id=city)
                        provice_instance = Area.objects.get(id=provice)

                        cities = Area.objects.filter(parent_id=city_instance.parent_id)
                        counties = Area.objects.filter(parent_id=city_instance.id) 
                        content['cities'] = cities
                        content['counties'] = counties 

                        content['county'] = ''
                        content['city'] = city_instance # 市
                        content['provicearea'] = provice_instance
                        if storetype == '0':
                            depts = depts.filter(area__parent_id = city_instance.id)
                        else:
                            depts = depts.filter(area__parent_id = city_instance.id, dept_type=storetype)
                        
                    except Area.DoesNotExist: 
                        #　根据省搜索
                        try: 
                            provice_instance = Area.objects.get(id=provice) 
                            cities = Area.objects.filter(parent_id=provice_instance.id) 
                            content['cities'] = cities 
                            cities_id = []
                            for cityitem in cities:
                                cities_id.append(cityitem.id) 
                            content['county'] = ''
                            content['city'] = city # 市
                            content['provicearea'] = provice_instance 
                            if provice == '110100':
                                if storetype == '0':
                                    depts = depts.filter(area__in = cities_id)
                                else:
                                    depts = depts.filter(area__in = cities_id, dept_type=storetype) 
                            else:
                                if storetype == '0':
                                    depts = depts.filter(area__parent_id__in = cities_id)
                                else:
                                    depts = depts.filter(area__parent_id__in = cities_id, dept_type=storetype) 
                                
                        except  Area.DoesNotExist:  
                            depts = depts.filter( area__id = '110100' )
                            area = Area.objects.get(pk='110100')
            else:
                depts = depts.filter(Q(area__parent_id = '110100') | Q(area__id = '110100') )
                provice_instance = Area.objects.get(pk='110100')

            provices = get_provice_list(request)
            provices_json = byte2json(provices.content)
           
            content['provices'] = provices_json
            content['depts'] = depts
            content['area'] = provice_instance

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
            and 'address' in request.POST  and 'area' in request.POST \
            and 'data_type' in request.POST : 
            name = request.POST['name'].strip() 
            storetype = request.POST['storetype'].strip() 
            phone = request.POST['phone'].strip() 
            detail = request.POST['detail'].strip() 
            address = request.POST['address'].strip() 
            areaid = request.POST['area'].strip() 
            data_type = request.POST['data_type'].strip() 
            area = Area.objects.get(id = areaid)

            # 创建Block 
            dept = models.Dept.objects.create(
                user = user, 
                name = name ,
                dept_type = int(storetype) ,
                phone = phone ,
                detail = detail,
                area = area,
                address = address,
                store_type=data_type
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

