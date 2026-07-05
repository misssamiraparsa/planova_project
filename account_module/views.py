from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import RegisterForm
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
            return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)



