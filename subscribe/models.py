#! -*- coding:utf-8 -*- 
from django.db import models
from appuser.models import AdaptorUser as User  
from django.utils.translation import ugettext_lazy as _ 
from basedatas.models import BaseDate
from django.db.models import F
from ckeditor_uploader.fields import RichTextUploadingField
from area.models import Area
class Subscribe(BaseDate): 
    """订阅功能"""
    email = models.CharField(max_length = 255, unique=True) 
    name = models.CharField(_('name'), max_length = 2048)
    
    def __str__(self):
        return self.name  
  