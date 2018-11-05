from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.views.generic import View
import re
def register(request):
    """注册"""
    if request.method  == "GET":
        # 返回注册页面
        return render(request,"users/db_register.html")
    else:
        # 进行注册处理
        # 接收数据
        email = request.POST.get('form_email')
        password = request.POST.get('form_password')
        username = request.POST.get('form_name')
        form_phone = request.POST.get('form_phone')
        form_yzm = request.POST.get('form_yzm')

        # 进行数据校验
        if not all([email, password, username,form_phone,form_yzm]):
            # 数据不完整
            return render(request, 'users/db_register.html', {'merror': '请把数据填写完整'})

        if not re.findall(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            # 判断提交的邮箱地址是否规范
            return render(request, 'users/db_register.html', {'merror': '请填写正确的邮箱地址'})

        if not re.findall(r'^1(3|4|5|7|8)\d{9}$', form_phone):
            # 判断提交的邮箱地址是否规范
            return render(request, 'users/db_register.html', {'merror': '请填写正确的手机号'})

        try:
            #判断用户名是否以及被注册
            User.objects.get(username=username)
        except:
            # 进行用户的注册
            user = User.objects.create_user(username,email,password,form_phone=form_phone,form_yzm=form_yzm)
            user.is_active=0  #表示账户未激活
            user.save()
            # 发送邮件给用户进行激活验证。
            # send_register_active_email.delay(email,user.username)
            return HttpResponse('注册成功')
        else:
            return render(request, 'users/db_register.html', {'merror': '该用户名已被注册'})

def login(View):
    """用户登陆"""
    return render(request,"users/db_login.html")