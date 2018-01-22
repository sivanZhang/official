from django.conf.urls import   url 
from dept.views import DeptView

 
urlpatterns = [  
    url(r'^list/$', DeptView.as_view(), name='list'),             
]
