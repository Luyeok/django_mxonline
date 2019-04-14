"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import xadmin
from django.views.generic import TemplateView

from users.views import LoginView, RegisterView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 直接返回index.html静态页面。
    # 对于纯静态的页面，就采用这样的方法来返回。
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    # 当使用类里面的View函数的时候，我们往往是使用类当中的as_view方法，这个方法返回了一个函数的句柄；
    path('register/', RegisterView.as_view(),name="register"),
    path('captcha/', include('captcha.urls')),
]
