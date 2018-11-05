from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser,BaseModel):
    """用户模型类"""
    form_phone = models.CharField(max_length=11,verbose_name="手机号")
    form_yzm = models.CharField(max_length=6,verbose_name="验证码")

    class Meta:
        db_table = 'dbmv_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name