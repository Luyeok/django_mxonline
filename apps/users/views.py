from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

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
                login(request, user)
                return render(request, "index.html")
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
