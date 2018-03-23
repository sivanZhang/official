from django.shortcuts import render
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
from django.conf import settings
from sitecontent.models import AdaptorBaseBlock

dmb     = DetectMobileBrowser()
 
def home(request):
    content ={}
    isMble  = dmb.process_request(request)

    sitecontents = AdaptorBaseBlock.objects.all() 
    content['sitecontents'] = sitecontents
    content['mediaroot'] = settings.MEDIA_URL

    if isMble:
        return render(request, 'en/home.html',content) 
    else:
        return render(request, 'en/home.html',content) 

def watch(request):
    content ={}
    isMble  = dmb.process_request(request)  
    content['mediaroot'] = settings.MEDIA_URL
    content['productpage'] = True
    if isMble:
        return render(request, 'en/watch.html',content) 
    else:
        return render(request, 'en/watch.html',content) 

def aboutus(request):
    content ={}
    isMble  = dmb.process_request(request)

    sitecontents = AdaptorBaseBlock.objects.all() 
    content['sitecontents'] = sitecontents
    content['mediaroot'] = settings.MEDIA_URL

    if isMble:
        return render(request, 'm_home.html',content) 
    else:
        return render(request, 'home.html',content) 


def contactus(request):
    content ={}
    isMble  = dmb.process_request(request)

    sitecontents = AdaptorBaseBlock.objects.all() 
    content['sitecontents'] = sitecontents
    content['mediaroot'] = settings.MEDIA_URL

    if isMble:
        return render(request, 'm_home.html',content) 
    else:
        return render(request, 'home.html',content) 

def accessories(request):
    content ={}
    isMble  = dmb.process_request(request) 
    content['mediaroot'] = settings.MEDIA_URL
    content['servicepage'] = True
    if isMble:
        return render(request, 'en/fetting.html',content) 
    else:
        return render(request, 'en/fetting.html',content) 

      

def parameters(request):
    content ={}
    isMble  = dmb.process_request(request) 
    content['mediaroot'] = settings.MEDIA_URL
    content['parameters'] = True

    if isMble:
        return render(request, 'en/accessories.html',content) 
    else:
        return render(request, 'en/accessories.html',content) 