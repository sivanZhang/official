from django.conf.urls import   url  
from book import views
 
urlpatterns = [  
    url(r'^buy/$', views.BookView.as_view(), name='buy'),            
]
