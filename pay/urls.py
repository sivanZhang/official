from django.conf.urls import include, url 
from pay import views
urlpatterns = [     
    url(r'^weixin/', views.weixin, name='weixin'),     
]
