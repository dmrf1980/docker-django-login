from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from .views import BienvenidaView, SignUpView, SignInView, SignOutView


class ResetPasswordView:
    pass


urlpatterns = [
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),

    path('password-reset/', PasswordResetView.as_view(template_name='login/password_reset_form.html'),
         name='password_reset'),

    path('password_reset_done', PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),
         name='password_reset_complete'),

]
