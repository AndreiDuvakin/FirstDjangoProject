from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
import django.contrib.auth.views as views
import django.forms
from django.urls import path, reverse_lazy

import users.views


def custom_auth_form(form):
    class CustomForm(form):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.visible_fields():
                if isinstance(field.field.widget, django.forms.CheckboxInput):
                    field.field.widget.attrs["class"] = "form-check-input"
                else:
                    field.field.widget.attrs["class"] = "form-control"

    return CustomForm


app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(
            template_name="users/login.html",
            authentication_form=custom_auth_form(AuthenticationForm),
            extra_context={
                "title": "Авторизация",
                "header_title": "Авторизация",
                "button_text": "Войти",
            },
        ),
        name="login",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(
            template_name="users/logout.html",
        ),
        name="logout",
    ),
    path(
        "password_change/",
        views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            form_class=custom_auth_form(PasswordChangeForm),
            extra_context={
                "title": "Смена пароля",
                "header_title": "Смена пароля",
                "button_text": "Сменить",
            },
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html",
            extra_context={
                "title": "Пароль изменен",
                "header_title": "Пароль изменен",
            },
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        views.PasswordResetView.as_view(
            template_name="users/password_reset.html",
            form_class=custom_auth_form(PasswordResetForm),
            success_url=reverse_lazy("users:password_reset_done"),
            extra_context={
                "title": "Сброс пароля",
                "header_title": "Сброс пароля",
                "button_text": "Сбросить",
            },
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_complete.html",
            extra_context={
                "title": "Сброс пароля",
                "header_title": "Ссылка для изменения "
                "пароля отправлена вам на почту",
            },
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            form_class=custom_auth_form(SetPasswordForm),
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_confirm_complite"),
            extra_context={
                "title": "Сброс пароля",
                "button_text": "Подтвердить",
            },
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_confirm/done/",
        views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
            extra_context={
                "title": "Пароль сброшен",
                "header_title": "Пароль сброшен",
            },
        ),
        name="password_reset_confirm_complite",
    ),
    django.urls.path(
        "signup/",
        users.views.signup,
        name="signup",
    ),
    django.urls.path(
        "activate/<str:username>/",
        users.views.activate,
        name="activate",
    ),
    django.urls.path(
        "users/<int:pk>/",
        users.views.user_detail,
        name="user_detail",
    ),
    path(
        "users/",
        users.views.user_list,
        name="user_list",
    ),
    path(
        "profile/",
        users.views.profile,
        name="profile",
    ),
]

__all__ = []
