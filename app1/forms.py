from django import forms
from .models import Rsetting,Ruser
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
    username=forms.CharField(label='نام کاربری',widget=forms.TextInput(attrs={'class': ' input100' }))
    password1 = forms.CharField(label='گذرواژه',widget=forms.PasswordInput(attrs={'class':"input100"}))
    password2 = forms.CharField(label='تکرار گذرواژه',widget=forms.PasswordInput(attrs={'class': 'input100' }))
    last_name = forms.CharField(label='نام و نام خانوادگی',widget=forms.TextInput(attrs={'class': 'input100' }))
    email = forms.EmailField(label='ایمیل',widget=forms.TextInput(attrs={'class': 'input100' }))
    personeli = forms.IntegerField(label='شماره پرسنلی',widget=forms.NumberInput(attrs={'class': 'input100' }))
    mobile = forms.IntegerField(label='شماره همراه',widget=forms.TextInput(attrs={'class': 'input100' }))
    dastmozd = forms.IntegerField(label='دستمزد',widget=forms.NumberInput(attrs={'class': 'input100' }))
    class Meta:
        model = Ruser
        fields = ['username', 'password1' , 'password2', 'email','last_name','personeli','mobile','dastmozd']

class Rsettingform(forms.ModelForm):
    class Meta:
        model = Rsetting
        fields = "__all__"
