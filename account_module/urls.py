from . import views
from django.urls import path

urlpatterns = [
    path('',views.RegisterView.as_view(),name='register_page'),
    path('login',views.LoginView.as_view(),name='login_page'),
    path('forgotPass',views.ForgotPassView.as_view(),name='forgot_page'),
    path('resetPass/<int:user_id>/<str:token>/',views.ResetPassView.as_view(),name='reset-password'),
]
