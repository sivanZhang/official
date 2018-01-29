#! -*- coding:utf-8 -*- 
from django.db import models
from appuser.models import AdaptorUser as User  
from django.utils.translation import ugettext_lazy as _ 
from basedatas.models import BaseDate
from django.db.models import F
from ckeditor_uploader.fields import RichTextUploadingField
from area.models import Area
class Dept(BaseDate):
    AFFILIATE = 1
    FLAGSHIP = 2
    DISTRIBUTE = 3
     
    STORE_CHOICES = (
        (AFFILIATE, _('Affiliate')),
        (FLAGSHIP, _('Flagship Store')),
        (DISTRIBUTE, _('Distribution Points')) 
    )

    # 是否允许永久删除产品，即从数据库中删除产品
    # 可以根据不同客户的不同需求具体确定
    # 如果 ALLOW_DELETE = True的时候代表可以删除
    # 如果 ALLOW_DELETE = False的时候代表不可以永久删除，status字段应该被设置为DELETED
    # 这主要是针对有订单产生的产品，没有订单产生的产品可以永久删除，而不在意ALLOW_DELETE的设置
    ALLOW_DELETE = True

    # 服务网点：1
    # 体验店： 0
    store_type = models.SmallIntegerField(default=0)
    
    # 体验店名称
    name = models.CharField(_('title'), max_length = 2048)
    # 地址
    area = models.ForeignKey(Area)
    address = models.CharField(_('detail address'), max_length = 2048, null = True)
    # 创建者
    user = models.ForeignKey(User)
    
    # 店铺类型
    dept_type = models.SmallIntegerField(default=AFFILIATE, choices=STORE_CHOICES)
    # 详情
    detail = RichTextUploadingField(_('Detail'), null=True)
    # 电话
    phone = models.CharField(_('Phone'), max_length = 128, null = True) 
    longitude = models.CharField(_('经度'), max_length = 64, null = True)
    latitude = models.CharField(_('纬度'), max_length = 64, null = True) 
    
    def __str__(self):
        return self.name  
  