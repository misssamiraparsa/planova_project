from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


def register(request):
    return render(request, 'account_module/register.html')

