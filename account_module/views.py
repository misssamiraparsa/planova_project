from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import RegisterForm, LoginForm
from .models import CustomUser


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = CustomUser.objects.create_user(
                fullname=register_form.cleaned_data['fullname'],
                username=register_form.cleaned_data['username'],
                email=register_form.cleaned_data['email'],
                phone_number=register_form.cleaned_data['phone_number'],
                parent_email=register_form.cleaned_data['parent_email']
            )
            user.set_password(register_form.cleaned_data['password'])
            user.save()
            return redirect(reverse('home_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context,)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = CustomUser.objects.filter(email__iexact=email).first()

            if user is None:
                login_form.add_error(None, 'کاربر با این مشخصات وجود ندارد.')
            else:
                is_password_correct = user.check_password(password)
                if is_password_correct:
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    return redirect(reverse('register_page'))
                else:
                    login_form.add_error(None,'ایمیل یا رمزعبور اشتباه وارد شده است')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html')
