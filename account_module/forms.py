from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator, MinLengthValidator, EmailValidator, MaxLengthValidator

from planova_project.account_module.models import CustomUser


class RegisterForm(forms.Form):
    fullname = forms.CharField(
        label='نام و نام خانوادگی'
    )
    username = forms.CharField(
        label='نام کاربری کاربر',
        initial='user1234',
        validators=[
            RegexValidator(r'^[a-zA-Z0-9]+$', 'فقط حروف و عدد'),
            MinLengthValidator(5)
        ]
    )
    email = forms.EmailField(
        label='ایمیل کاربر',
        widget=forms.EmailInput(),
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(),
        validators=[
            MinLengthValidator(8),

        ]
    )
    phone_number = forms.CharField(
        label='تلفن همراه',
        validators=[
            RegexValidator(r'^0\d{10}$', 'شماره موبایل معتبر نیست (مثل ۰۹۱۲۳۴۵۶۷۸۹)')
        ]
    )
    parent_email = forms.EmailField(
        label='ایمیل والد',
        widget=forms.EmailInput(),
    )

    def clean_username(self):
        context = self.cleaned_data['username']
        if CustomUser.objects.filter(username=context).exists():
            raise forms.ValidationError('این نام کاربری از قبل وجود دارد.')
        return context

    def clean_email(self):
        context = self.cleaned_data['email']
        if CustomUser.objects.filter(email=context).exists():
            raise forms.ValidationError('کاربری با این ایمیل از قبل وجود دارد.')
        return context

    def clean_parent_email(self):
        context = self.cleaned_data['parent_email']
        if CustomUser.objects.filter(parent_email=context).exists():
            raise forms.ValidationError('والدی با این ایمیل از قبل وجود دارد.')
        return context

    def clean_phone_number(self):
        context = self.cleaned_data['phone_number']
        if CustomUser.objects.filter(phone_number=context).exists():
            raise forms.ValidationError('این تلفن همراه از قبل وجود دارد.')
        return context

    def clean_password(self):
        context = self.cleaned_data['password']
        validate_password(context)
        return context
