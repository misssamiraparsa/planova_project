from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .utils import send_email
from .forms import RegisterForm, LoginForm, ForgotPassForm
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
        return render(request, 'account_module/register.html', context, )


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
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    remember_me = request.POST.get('remember_me')
                    if remember_me:
                        request.session.set_expiry(1209600)
                    else:
                        request.session.set_expiry(0)
                    return redirect(reverse('register_page'))
                else:
                    login_form.add_error(None, 'ایمیل یا رمزعبور اشتباه وارد شده است')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgotPassView(View):
    def get(self, request):
        forget_pass_form = ForgotPassForm()
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request):
        forget_pass_form = ForgotPassForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()
            if user is not None:
                token = PasswordResetTokenGenerator().make_token(user)
                link = f"http://127.0.0.1:8000/reset-password/{user.id}/{token}/"
                send_email('بازیابی کلمه عبور', user.email, {'user': user, 'link':link}, 'emails/forgot_password.html')
                messages.success(request, 'لینک بازیابی رمز عبور با موفقیت به ایمیل شما ارسال شد.')
                return redirect('register_page')
        messages.error(request, 'لطفاً ایمیل معتبری وارد کنید.')
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account_module/forgot_password.html', context)

