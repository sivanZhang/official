from django.conf.urls import   url 
 
from subscribe import views
 
urlpatterns = [  
    url(r'^list/$', views.SubscribeView.as_view(), name='list'),          
    url(r'^send/$', views.send, name='send')    
]
