from django.conf.urls import   url 
from page.views import PageView 


urlpatterns = [  
    url(r'^(?P<blockname>[a-zA-Z0-9]+)/(?P<pagename>[a-zA-Z0-9]+)/$', PageView.as_view(), name='page'),             
]
