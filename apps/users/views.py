from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email

# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html",{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username= username
            user_profile.email=username
            user_profile.password=make_password(password)
            user_profile.is_active=False
            user_profile.save()
            send_register_email(username, "register")
            return render(request,'login.html')
        else:
            return render(request,'register.html',{"register_form":register_form})

class ActiveUserView(View):
    def get(self,request, active_code):
        all_records= EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email=record.email
                user = UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
            return render(request, "login.html")


# 使用类进行登陆
# django中，比较推荐使用这种基于类的视图函数
class LoginView(View):
    # 这里，因为我们继承了View类，里面的get 和 post函数自带基础的判断，
    # 所以，这里我们不需要对request返回的是GET还是POST进行判断
    def get(self,request):
        return render(request, "login.html", {})

    def post(self,request):
        login_form=LoginForm(request.POST)
        # 这里的LoginForm是用来验证表单有效性的。
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request,"login.html",{'msg':"用户未激活。"})
            else:
                return render(request,"login.html",{"msg":"用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try :
            user = UserProfile.objects.get(Q(username=username)|Q(
                email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 使用函数进行登陆
# def mylogin(request):
#     if request.method == "POST":
#         username=request.POST.get("username","")
#         password=request.POST.get("password","")
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             login(request, user)
#             return render(request,"index.html")
#         else:
#             return render(request,"login.html",{"msg":"用户名或密码错误！"})
#     elif request.method =="GET":
#         return render(request, "login.html",{})
