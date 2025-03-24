from django import forms
from captcha.fields import CaptchaField

class UserLoginForm(forms.Form):
    account = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

class UserRegForm(forms.Form):
    username = forms.CharField()