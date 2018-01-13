from django.conf.urls import include, url 
from product.views import ProductView, ProductDetailView
from product import views

urlpatterns = [  
    url(r'^products/$', ProductView.as_view(), name='products'),   
    url(r'^products/cast2/$',views.cast2, name='cast2'), 
    url(r'^products/castdock/$',views.castdock, name='castdock'), 
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailView.as_view(), name='detail'),  
    url(r'^products/(?P<pk>[0-9]+)/change$', views.change , name='change'),
]
