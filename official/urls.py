"""official URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from official import views
from official import en_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^pic/', include('piclab.urls', namespace="piclab")),
    url(r'^$', views.home, name='home'),
    url(r'^users/', include('appuser.urls', namespace="users")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^category/', include('category.urls', namespace="category")),
    url(r'^sitecontent/', include('sitecontent.urls', namespace="sitecontent")),
    url(r'^page/', include('page.urls', namespace="page")),
    url(r'^book/', include('book.urls', namespace="book")),
    url(r'^bussiness/', include('bussiness.urls', namespace="bussiness")),
    url(r'^area/', include('area.urls', namespace="area")),
    url(r'^dept/', include('dept.urls', namespace="dept")),
    url(r'^subscribe/', include('subscribe.urls', namespace="subscribe")),

    url(r'^$', views.home, name='home'),

    url(r'^en/home$', en_views.home, name='home'),
    url(r'^en/watch$', en_views.watch, name='watch'),
    url(r'^en/aboutus$', en_views.aboutus, name='aboutus'),
    url(r'^en/contactus$', en_views.contactus, name='contactus'),
    url(r'^en/accessories$', en_views.accessories, name='accessories'),
    url(r'^en/parameters$', en_views.parameters, name='parameters'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
