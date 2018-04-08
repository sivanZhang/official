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
                return render(request, 'page/m_aboutus.html', content)
            else:
                return render(request, 'page/aboutus.html', content)

        if 'asubrand' == blockname and 'enaboutus' == pagename:
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
                return render(request, 'en/aboutus.html', content)
            else:
                return render(request, 'en/aboutus.html', content)

        if 'asubrand' == blockname and 'encontactus' == pagename:  
            # 联系我们 
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
                return render(request, 'en/contactus.html', content)
            else:
                return render(request, 'en/contactus.html', content)

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
                return render(request, 'page/m_joinus.html', content)
            else:
                return render(request, 'page/joinus.html', content)
        if 'asubrand' == blockname and  'faith' == pagename:
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/m_faith.html', content)
            else:
                return render(request, 'page/faith.html', content)

        if 'policy' == blockname :
            # 保修政策
            try:
                block = models.AdaptorBaseBlock.objects.get(mark = blockname)
                content['pageblock'] = block
                url = block.url
                content['img'] =  block.pic.replace('\\','/')
                match = re.search('\d+', url)
                if match:
                    productid = match.group()
                    try:
                        product = AdaptorProduct.objects.get(id=productid)
                        content['product'] = product 
                    except AdaptorProduct.DoesNotExist:
                        raise Http404 
            except models.AdaptorBaseBlock.DoesNotExist:
                raise Http404 
            if isMble:
                return render(request, 'page/m_policy.html', content)
            else:
                return render(request, 'page/policy.html', content)
        if 'waiting' == blockname :
            # 敬请期待
            if isMble:
                return render(request, 'page/m_waiting.html', content)
            else:
                return render(request, 'page/waiting.html', content)
        if 'software' == blockname :
            # 软件下载
            if isMble:
                return render(request, 'page/m_software.html', content)
            else:
                return render(request, 'page/software.html', content)
        if 'questions' == blockname :
            # 常见问题
            # 获得热点问题
            content['servicepage'] = True
            if 'hot' in request.GET:
                hot_products = AdaptorProduct.objects.filter(category__name = "热点问题")
                content['hot_products'] = hot_products 
                if isMble:
                    return render(request, 'page/questions.html', content)
                else:
                    return render(request, 'page/questions.html', content)
            else:
                # 获得使用小技巧
                skill_products = AdaptorProduct.objects.filter(category__name = "使用小技巧")
                content['skill_products'] = skill_products 
                if isMble:
                    return render(request, 'page/skill.html', content)
                else:
                    return render(request, 'page/skill.html', content)

             

        if 'service' == blockname and 'list' == pagename:
            contentblock = models.AdaptorBaseBlock.objects.filter(mark=blockname)
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['contentblock'] = contentblock[0]
            # 获得热点问题
            hot_products = AdaptorProduct.objects.filter(category__name = "热点问题")
            # 获得使用小技巧
            skill_products = AdaptorProduct.objects.filter(category__name = "使用小技巧")

            content['hot_products'] = hot_products[:5]
            content['skill_products'] = skill_products[:5]
            content['servicepage'] = True
            if isMble:
                return render(request, 'page/m_service.html', content)
            else:
                return render(request, 'page/service.html', content)
        if 'news' == blockname :
            # 新闻
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark = blockname)
            
            if len(pages) == 0:
                raise Http404
            content['pages'] = pages 
            pagesitems = pages.exclude(mark = 'bigimg')
             
            # 分页开始
            counter = pagesitems.count()
            pagesize = 10
            pageindex = request.GET.get('pageindex')
            try:
                pageindex = int(pageindex)
            except TypeError:
                pageindex = 1
            except ValueError:
                pageindex = 1
            content['pagecurrent'] = pageindex 
             
            content['contentblock'] = pages[0].block
            labels_list = []
            for page in pages:
                if page.lables:
                    labels_list += page.lables.split(',')
         
            labels_list = list(set(labels_list))
            content['labels_list'] = labels_list
            if isMble: 
                pagesize = 2
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/m_news.html', content)
            else: 
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/news.html', content)

        if 'video' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['block'] = pages[0].block
            content['pages'] = replace_slide(pages)

            # 分页开始
            pagesitems = pages
            counter = pagesitems.count()
            pagesize = 10
            pageindex = request.GET.get('pageindex')
            try:
                pageindex = int(pageindex)
            except TypeError:
                pageindex = 1
            except ValueError:
                pageindex = 1
            content['pagecurrent'] = pageindex 

            if isMble:
                pagesize = 2
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/m_video.html', content)
            else:
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/video.html', content)
        if 'contactus' == blockname :
            # 联系我们 
            try:
                block = models.AdaptorBaseBlock.objects.get(mark = blockname)
                content['block'] = block
                url = block.url
                match = re.search('\d+', url)
                if match:
                    productid = match.group()
                    try:
                        product = AdaptorProduct.objects.get(id=productid)
                        content['product'] = product
                        content['block'] = block
                    except AdaptorProduct.DoesNotExist:
                        raise Http404 
            except models.AdaptorBaseBlock.DoesNotExist:
                raise Http404
            if isMble:
                return render(request, 'page/m_contactus.html', content)
            else:
                return render(request, 'page/contactus.html', content)
 
        if 'report' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['contentblock'] = pages[0].block
            content['pages'] = replace_slide(pages)
            labels_list = []
            for page in pages:
                if page.lables:
                    labels_list += page.lables.split(',')
         
            labels_list = list(set(labels_list))
            content['labels_list'] = labels_list

            # 分页开始 
            pagesitems =  pages
            counter = pagesitems.count()
            pagesize = 10
            pageindex = request.GET.get('pageindex')
            try:
                pageindex = int(pageindex)
            except TypeError:
                pageindex = 1
            except ValueError:
                pageindex = 1
            content['pagecurrent'] = pageindex 


            if isMble:
                pagesize = 2
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/m_report.html', content)
            else:
                maxpage = int(counter/pagesize)
                content['pagescounter'] = range(maxpage)
                content['maxpage'] = maxpage
                content['pageitems'] = pagesitems[pagesize*(pageindex-1):pagesize*pageindex]
                return render(request, 'page/report.html', content)
        if 'pic' == blockname :
            # 媒体报道
            pages = models.AdaptorBaseBlockItem.objects.filter(block__mark=blockname)
            content['page'] = pages[0]
            content['pages'] = replace_slide(pages)
            if isMble:
                return render(request, 'page/m_pic.html', content)
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
                    for eventyear in content['eventyears']:
                        if eventyear['year'] == year:
                            eventyear['pages'].append(page)
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
                return render(request, 'page/m_eventlist.html', content)
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
                if not page.date:# 精彩活动中，不填写日期的不显示
                    continue 

                match = re.search('\d+', url)
                if match:
                    productid = match.group()
                    try:
                        product = AdaptorProduct.objects.get(id=productid)
                        year = page.date.year
                        product.date = page.date
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
                return render(request, 'page/m_activelist.html', content)
            else:
                return render(request, 'page/activelist.html', content)
        if 'detail' == pagename:
            if isMble:
                return render(request, 'page/m_detail.html', content)
            else:
                return render(request, 'page/m_detail.html', content)
        if 'software' == pagename:
            if isMble:
                return render(request, 'page/m_software.html', content)
            else:
                return render(request, 'page/software.html', content)
        if 'usage' == pagename:
            if isMble:
                return render(request, 'page/usage.html', content)
            else:
                return render(request, 'page/usage.html', content)
        else:
            raise Http404

def replace_slide(pages):
    for page in pages:
        page.pic = page.pic.replace('\\','/')
    
    return pages

        