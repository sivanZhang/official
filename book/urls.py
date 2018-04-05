from django.conf.urls import   url  
from book import views
from book import views_pay 
urlpatterns = [  
    url(r'^buy/$', views.BookView.as_view(), name='buy'),         
    url(r'^alipay_check_pay/$', views_pay.alipay_check_pay, name='alipay_check_pay'),   
    url(r'^alipay_notify/$', views_pay.alipay_notify, name='alipay_notify'), 
]
