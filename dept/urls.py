from django.conf.urls import   url 
 
from dept import views
 
urlpatterns = [  
    url(r'^list/$', views.DeptView.as_view(), name='list'),          
    url(r'^send/$', views.send, name='send')    
]
