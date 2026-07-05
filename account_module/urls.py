from . import views
from django.urls import path

urlpatterns = [
    path('',views.RegisterView.as_view(),name='register_page'),
]
