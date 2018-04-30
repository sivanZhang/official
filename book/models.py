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
    billno = models.CharField(_('bill No.'), max_length = 255, unique = True)
    email = models.CharField(_('email'), max_length = 512, null = True) 
    address = models.CharField(_('address'), max_length = 1024) 
    
    # 状态
    # 0 创建成功但未支付
    # 1 已支付
    # 2 已完成
    STATUS_CREATED = 0 # 创建成功但未支付
    STATUS_PAYED = 1 # 已支付
    STATUS_USED = 2 # 已使用

    status = models.SmallIntegerField(default = STATUS_CREATED) 

    # 支付信息
    ALIPAY = 'zhifubao' #支付宝
    WEIXINPAY = 'weixin' #微信
 
    PAY_CHOICES = (
        (WEIXINPAY, '微信'),
        (ALIPAY, '支付宝'), 
    )
    # 支付方式
    pay_way = models.CharField( choices=PAY_CHOICES, max_length = 128, null =True)
    # 支付金额
    payed_money = models.DecimalField(_('Payed Money'), max_digits = 9, decimal_places = 2, null =True)
    # 微信或者支付宝的支付编号
    trade_no = models.CharField(_('trade no'), max_length = 4096, null = True) 
    pay_datetime = models.DateTimeField(_('pay date'), null = True) 

    class Meta:
        abstract = True
        
class AdaptorBook(Book):
    pass



