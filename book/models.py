# -*- coding:utf-8 -*-
from django.db import models
from appuser.models import AdaptorUser as User
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    """
    预约模块
    """
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    name = models.CharField(_('name'), max_length = 1024 )
    phone = models.CharField(_('phone'), max_length = 1024)
    # 订单号
    billno = models.CharField(_('bill No.'), max_length = 1024, null= True)
    email = models.CharField(_('email'), max_length = 512, null = True) 
    address = models.CharField(_('address'), max_length = 1024) 
    
    # 状态
    # 0 创建成功但未支付
    # 1 已支付
    # 2 已完成
    status = models.SmallIntegerField(default = STATUS_SHOW) 
    # 支付方式（支付宝，微信）以及订单号
    payed_way = models.CharField(_('payed way'), max_length = 512, null = True) 
    payed_no = models.CharField(_('address'), max_length = 512, null = True) 
  
    class Meta:
        abstract = True
        
class AdaptorBook(Book):
    pass



