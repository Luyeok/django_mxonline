from django import forms
class LoginForm(forms.Form):
    # 这里的Form 只是用来验证我们的表单填写规则
    # 这里就是用来定义规则的；
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)