from django.conf.urls import   url  
from bussiness import views
 
urlpatterns = [  
    url(r'^new/$', views.BussinessView.as_view(), name='new'),            
]
