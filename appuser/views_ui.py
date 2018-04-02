# -*- coding: utf-8 -*-
import requests
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect 
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import  Group
import os
from appuser.models import AdaptorUser as User
from appuser.models import VerifyCode
import json
import random
import string
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import UploadPortrainForm, GroupForm, UserForm
from django.contrib import auth
from official.third_party_backend import authenticate
#from socialoauth import SocialSites,SocialAPIError  

from basedatas.bd_comm import Common
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

dmb     = DetectMobileBrowser()
comm    = Common()

@csrf_exempt
def login(request):
    # 第三方登录开始
    if 'token' in request.GET:
        token = request.GET['token']
        appid = settings.LOGIN_APPID
        secret = settings.LOGIN_SECRET
        post_data = { 'token' : token,
                  'appid' : appid,
                  'secret' : secret
                }
                  
        req = requests.post(settings.THIRD_AUTH_URL, data = post_data)
        
        if req.status_code == 200:
            userinfo = json.loads(req.text)
            if userinfo['status'] == 'ok':
                userinfo  = userinfo['result']
                phone = userinfo['phone'] 
                email = userinfo['email'] 
                username = userinfo['username']   
                try:
                    user = User.objects.get(phone = phone)  
                except User.DoesNotExist: 
                    password = str(uuid.uuid4())
                  
                    user = User(username= username, phone=phone, email = '',  password=password)
                    if email:
                        user.email = email
                    user.save() 
                  
                #log the User in our web site
                auth.logout(request)  
                user =  authenticate(phone = phone) 
                request.user = user 
                auth.login(request, user) 
                if 'next' in request.GET: 
                    next_url = request.GET.get('next')
                else:
                    next_url = '/'
                return redirect(next_url )
            else:
                return HttpResponse(userinfo['msg']) 
        else:
            return HttpResponse("用户认证系统异常...") 
    else:
        return redirect(settings.THIRD_LOGIN_URL )
    # 第三方登录结束

    isMble  = dmb.process_request(request)
    
    if 'email' in request.POST and 'password' in request.POST:
            auth.logout(request)
            email       = request.POST['email']
            password      = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            if 'next' in request.GET: 
                next_url = request.GET.get('next')
            else:
                next_url = request.POST.get('next')
            context ={} 
            if user:
                # User is valid.  Set request.user and persist user in the session
                # by logging the user in.
                request.user = user
                auth.login(request, user)
                # redirect to the value of next if it is entered, otherwise
                # to settings.APP_WEB_PC_LOGIN_URL
               
                if next_url:
                    #after login, return to the previous page, but if the previous page is logout, 
                    #then return to the host page
                    if 'logout' not in str(next_url): 
                         return redirect(next_url)
                    else:
                        return redirect(reverse('home'))
                else:
                    return redirect(reverse('home'))
            else:
                try: 
                    user_instance = User.objects.get(email = email)
                    msg = '登录失败，密码错误...' 
                except User.DoesNotExist:
                    msg = '登录失败，用户{0}未注册...'.format(email)
          
                context = {'next':next_url,
                           'status':'error',
                           'msg':msg,
                           'email':email}
            if isMble: 
                return render(request, 'user/m_login.html', context)
            else:
                return render(request, 'user/login.html', context)
            
    else:
        next_url = request.GET.get('next')
        context = {'next':next_url}

        if isMble: 
            return render(request, 'user/m_login.html', context)
        else:  
            return render(request, 'user/login.html', context)

def logout(request):
    auth.logout(request)
    isMble  = dmb.process_request(request)
    return redirect(reverse('home'))
   
@csrf_exempt
def register(request):
    isMble  = dmb.process_request(request)
    content = {}
    
    if request.method == "POST":  
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        emailcode = request.POST['emailcode'].strip()
        if VerifyCode.objects.veirfy_code(emailcode, email):
            user = User.objects.create_user(email, username,  password)
            content={
                'result':'ok',
                'msg':'注册成功！'
            }
        else:
            content={
                'result':'error',
                'username':username,
                'email':email, 
                'msg':'验证码错误...'
            }
    
    if isMble: 
        return render(request, 'user/m_regsiter.html', content)
    else:  
        return render(request, 'user/regsiter.html', content)

@login_required
def mine(request):
    isMble  = dmb.process_request(request)
    
    user = request.user
    content = {
        'user':user,
        'mine':'menu-act'
        }
    if isMble: 
        return render(request, 'user/m_mine.html', content)
    else:  
        return render(request, 'user/mine.html', content)