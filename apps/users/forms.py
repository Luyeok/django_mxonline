from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    # 这里的Form 只是用来验证我们的表单填写规则
    # 这里就是用来定义规则的；
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})
    # 可以使用form 来定制参数信息；