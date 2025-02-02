from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text="أدخل رقم الهاتف بصيغة صحيحه")
    cr_number = forms.CharField(max_length=20, required=False, help_text="رقم السجل التجاري (للملاك فقط)")
    signature = forms.ImageField(required=False, help_text="تحميل التوقيع الإلكتروني")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'cr_number', 'role', 'signature']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'cr_number', 'signature']