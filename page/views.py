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
from django.views.generic.detail import DetailView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from django.utils.translation import ugettext as _

from sitecontent import models
from product.models import AdaptorProduct

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
dmb     = DetectMobileBrowser()

class PageView(View):
    """
    内容管理
    """
    def get(self, request, blockname, pagename):
        isMble  = dmb.process_request(request)
        content = {}   
        content['mediaroot'] = settings.MEDIA_URL
        if 'asubrand' == blockname and 'aboutus' == pagename:
            products = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            if isMble:
                return render(request, 'page/aboutus.html', content)
            else:
                return render(request, 'page/aboutus.html', content)

        if 'test' == pagename:
            if isMble:
                return render(request, 'page/test.html', content)
            else:
                return render(request, 'page/test.html', content)
        if 'detail' == pagename:
            if isMble:
                return render(request, 'page/m_detail.html', content)
            else:
                return render(request, 'page/m_detail.html', content)
        else:
            raise Http404

     