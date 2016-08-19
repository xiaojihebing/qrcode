# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Products(models.Model):
    tinyurl = models.CharField(u'产品标识', max_length=50, unique=True)
    pro_name = models.CharField(u'产品名称', max_length=250)
    pro_brand = models.CharField(u'品牌', max_length=50,blank=True)
    pro_model = models.CharField(u'型号', max_length=50,blank=True)
    pro_price = models.CharField(u'零售价', max_length=50,blank=True)
    pro_capacity = models.CharField(u'容量', max_length=50,blank=True)
    pro_input = models.CharField(u'输入', max_length=50,blank=True)
    pro_output = models.CharField(u'输出', max_length=50,blank=True)
    pro_company = models.CharField(u'生产厂家', max_length=50,blank=True)
    pro_add = models.CharField(u'工厂地址', max_length=250,blank=True)
    pro_phone = models.CharField(u'客服热线', max_length=50,blank=True)
    pro_url = models.CharField(u'官方网站', max_length=250,blank=True)
    pro_color = models.CharField(u'颜色', max_length=50,blank=True)
    pro_size = models.CharField(u'尺寸', max_length=50,blank=True)
    pro_weight = models.CharField(u'重量', max_length=50,blank=True)
    pro_intro = models.TextField(u'产品介绍', blank=True)
    com_intro = models.TextField(u'公司介绍', blank=True)
    pro_other1 = models.CharField(max_length=250,blank=True)
    pro_other2 = models.CharField(max_length=250,blank=True)
    pro_other3 = models.CharField(max_length=250,blank=True)
    pro_other4 = models.CharField(max_length=250,blank=True)
    pro_other5 = models.CharField(max_length=250,blank=True)
    pro_other6 = models.CharField(max_length=250,blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = u'qr_products'
        verbose_name = u'产品'
        verbose_name_plural = u'产品管理'

    def __unicode__(self):
        return '%s: %s' % (self.tinyurl, self.pro_name)
