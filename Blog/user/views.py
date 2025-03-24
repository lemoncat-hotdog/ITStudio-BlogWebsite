from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from .forms import UserLoginForm
from .models import *

def login_view(request):
    if request.method == "POST":
        user_login = UserLoginForm(request.POST)
        user_login.account = request.POST['account']
        user_login.password = request.POST['password']
        if '@' in user_login.account:
            try:
                user = BlogUser.objects.get(email=user_login.account)
                user_login.account = user.username
            except BlogUser.DoesNotExist:
                return render(request, "Login.html", {
                    "error": "邮箱未注册，请先注册账号!"
                })

        user = authenticate(username=user_login.account, password=user_login.password)
        if user is None:
            return render(request, "Login.html", {
                "error": "不存在此账户！请先注册"
            })
        elif not user.is_active:
            return render(request, "Login.html", {
                "error": "此账户还未激活，请使用激活邮件激活！"
            })
        else:
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        user_login = UserLoginForm()
        return render(request, "Login.html", {"user_login": user_login})


