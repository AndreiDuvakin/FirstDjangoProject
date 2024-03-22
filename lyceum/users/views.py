import django.conf
import django.contrib
import django.contrib.auth
import django.contrib.auth.decorators
import django.core.mail
import django.shortcuts
import django.template.loader
import django.urls
import django.utils

import users.forms
import users.models


def user_list(request):
    users = django.contrib.auth.get_user_model().objects.filter(is_active=True)
    return django.shortcuts.render(
        request,
        "users/user_list.html",
        {"users": users, "title": "Список пользователей"},
    )


def user_detail(request, pk):
    user = django.shortcuts.get_object_or_404(
        django.contrib.auth.get_user_model(),
        pk=pk,
    )
    try:
        profile = user.profile
    except users.models.Profile.DoesNotExist:
        profile = None

    return django.shortcuts.render(
        request,
        "users/user_detail.html",
        {"user": user, "profile": profile},
    )


@django.contrib.auth.decorators.login_required
def profile(request):
    user_form = users.forms.CustomUserChangeForm(
        request.POST or None,
        instance=request.user,
    )

    profile_form = users.forms.ProfileForm(
        request.POST or None,
        instance=request.user.profile,
    )

    if request.method == "POST":
        if all((profile_form.is_valid(), user_form.is_valid())):
            profile_form.save()
            user_form.save()

    return django.shortcuts.render(
        request,
        "users/profile.html",
        {
            "profile_form": profile_form,
            "user_form": user_form,
            "user": request.user,
        },
    )


def signup(request):
    form = users.forms.SignUpForm(request.POST or None)
    template = "users/signup.html"
    context = {
        "form": form,
        "header_title": "Регистрация",
        "title": "Регистрация",
        "button_text": "Зарегистрироваться",
    }
    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.is_active = django.conf.settings.DEFAULT_USER_IS_ACTIVE
        user.save()

        user.profile = users.models.Profile.objects.create(user_id=user.id)

        html_content = django.template.loader.render_to_string(
            "users/signup_email.html",
            {"username": form.cleaned_data["username"]},
        )

        msg = django.core.mail.EmailMultiAlternatives(
            subject="Activate your account",
            body=html_content,
            from_email=django.conf.settings.DJANGO_MAIL,
            to=[form.cleaned_data["email"]],
        )
        msg.content_subtype = "html"
        msg.send()
        django.contrib.messages.success(
            request,
            "Вы успешно зарегистрированы",
        )
        return django.shortcuts.redirect(django.urls.reverse("users:login"))

    return django.shortcuts.render(request, template, context)


def activate(request, username):
    user = django.shortcuts.get_object_or_404(
        django.contrib.auth.get_user_model().objects,
        username=username,
    )
    registration_time_limit = (
        django.utils.timezone.now() - django.utils.timezone.timedelta(hours=12)
    )

    if user.date_joined >= registration_time_limit:
        user.is_active = True
        user.save()
        django.contrib.messages.success(request, "Активация прошла успешно")
    else:
        django.contrib.messages.error(request, "Ошибка при активации")

    return django.shortcuts.redirect(django.urls.reverse("homepage:homepage"))


__all__ = []
