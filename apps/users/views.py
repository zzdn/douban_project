from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout

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


class Logins(View):
    """用户登陆"""
    def get(self,request):
        if request.user.is_authenticated():
            return redirect('/db_movie')

        cookie = request.COOKIES.get('form_email')
        print(cookie)
        if cookie==None:
            username =''
        else:
            username=cookie
        # 返回登陆页面
        return render(request,'users/db_login.html',{'form_name':username})

    def post(self, request):
        # 进行登陆验证
        # 获取登陆请求的用户信息
        username = request.POST.get('form_email')
        password = request.POST.get('form_password')
        remember = request.POST.get('remember')
        if not all([username, password]):
            # 判读请求数据是否完整
            return render(request, 'users/db_login.html', {'msg': '请把账号和密码填写完整'})

        # 进行校验账号密码
        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, 'users/db_login.html', {'msg': '您输入的账户或密码信息有误'})

        # 获取登陆后跳转的地址
        login(request, user)  # 通过session记住用户登陆状态
        next_url = request.GET.get('next', '/db_movie')
        if remember == 'on':
            # 判读是否有记住账号
            response = redirect(next_url)
            response.set_cookie('form_email', username)  # 通过cookie记住用户名

        else:
            response = redirect(next_url)
            response.delete_cookie('username')

        return response

def db_movie(request):
    return render(request,"movies/db_movie.html")