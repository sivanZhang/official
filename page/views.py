#! -*- coding:utf-8 -*-
import pdb
import re

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
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname, mark=pagename)
            if len(pages) == 0:
                raise Http404
            page_item = pages[0]
            url = page_item.url
            match = re.search('\d+', url)
            if match:
                productid = match.group()
                try:
                    product = AdaptorProduct.objects.get(id=productid)
                    content['product'] = product
                    page_item.pic = page_item.pic.replace('\\','/')
                    content['page'] = page_item
                    content['blockname'] = blockname
                except AdaptorProduct.DoesNotExist:
                    raise Http404
            if isMble:
                return render(request, 'page/aboutus.html', content)
            else:
                return render(request, 'page/aboutus.html', content)
        if 'asubrand' == blockname and 'join' == pagename:
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname, mark=pagename)
            if len(pages) == 0:
                raise Http404 
            page_item = pages[0]
            page_item.pic = page_item.pic.replace('\\','/')
             
            url = page_item.url
            match = re.search('\d+', url)
            if match:
                productid = match.group()
                try:
                    product = AdaptorProduct.objects.get(id=productid)
                    content['product'] = product
                    page_item.pic = page_item.pic.replace('\\','/')
                    content['page'] = page_item
                    content['blockname'] = blockname
                except AdaptorProduct.DoesNotExist:
                    raise Http404 
            if 'position' in request.GET and 'category' in request.GET:
                # 说明是在查看职位列表
                category = request.GET['category']
                content['page'] = page_item
                perm = False
                if request.user:
                    perm = request.user.has_perm('product.manage_product')
                content['perm'] = perm
                products = AdaptorProduct.objects.filter(category__parent__id = category)
                content['products'] = products
                if isMble:
                    return render(request, 'page/positions.html', content)
                else:
                    return render(request, 'page/positions.html', content)
            if isMble:
                return render(request, 'page/joinus.html', content)
            else:
                return render(request, 'page/joinus.html', content)
        if 'asubrand' == blockname and  'faith' == pagename:
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/faith.html', content)
            else:
                return render(request, 'page/faith.html', content)
        if 'service' == blockname and 'list' == pagename:
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/service.html', content)
            else:
                return render(request, 'page/service.html', content)
        if 'news' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/news.html', content)
            else:
                return render(request, 'page/news.html', content)
        if 'video' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/video.html', content)
            else:
                return render(request, 'page/video.html', content)
        if 'contactus' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages) 
            if isMble:
                return render(request, 'page/contactus.html', content)
            else:
                return render(request, 'page/contactus.html', content)
        if 'report' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/report.html', content)
            else:
                return render(request, 'page/report.html', content)
        if 'pic' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/pic.html', content)
            else:
                return render(request, 'page/pic.html', content)
        if 'event' == blockname and  'list' == pagename:
            # 获得所有大事记
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark = blockname)
            
            if len(pages) == 0:
                raise Http404
            content['pages'] = pages
            content['img'] = pages[0].block.pic.replace('\\','/')
            content['contentblock'] = pages[0].block
            content['eventyears'] = []
            page_item = pages[0]
            for page in pages: 
                if page.date:
                    year = page.date.year
                    mark = False
                    for activeyear in content['eventyears']:
                        if activeyear['year'] == year:
                            activeyear['pages'].append(page)
                            mark = True
                            break
                    if mark == False:
                        # 表示当前年份还没有被加入content['eventyears']这个列表
                        
                        tmp = {
                            'year':year,
                            'pages':[page]
                        }
                        content['eventyears'].append(tmp)
          
            if isMble:
                return render(request, 'page/eventlist.html', content)
            else:
                return render(request, 'page/eventlist.html', content)
        if 'active' == blockname and  'list' == pagename:
            # 获得所有精彩活动列表
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark = blockname)
            
            if len(pages) == 0:
                raise Http404
            content['pages'] = pages
            content['img'] = pages[0].block.pic.replace('\\','/')
            content['contentblock'] = pages[0].block
            content['activeyears'] = []
            page_item = pages[0]
            for page in pages: 
                url = page.url
                match = re.search('\d+', url)
                if match:
                    productid = match.group()
                    try:
                        product = AdaptorProduct.objects.get(id=productid)
                        year = product.date.year
                        mark = False
                        for activeyear in content['activeyears']:
                            if activeyear['year'] == year:
                                product.pageurl = page.pic
                                activeyear['products'].append(product)
                                mark = True
                                break
                            
                        if mark == False:
                            # 表示当前年份还没有被加入content['activeyears']这个列表
                            product.pageurl = page.pic
                            tmp = {
                                'year':year,
                                'products':[product]
                            }
                            
                            content['activeyears'].append(tmp) 
                    except AdaptorProduct.DoesNotExist:
                        # 忽略用户设置错误的活动
                        pass  
            if isMble:
                return render(request, 'page/activelist.html', content)
            else:
                return render(request, 'page/activelist.html', content)
        if 'detail' == pagename:
            if isMble:
                return render(request, 'page/m_detail.html', content)
            else:
                return render(request, 'page/m_detail.html', content)
        else:
            raise Http404

def replace_slide(pages):
    for page in pages:
        page.pic = page.pic.replace('\\','/')
    
    return pages

        