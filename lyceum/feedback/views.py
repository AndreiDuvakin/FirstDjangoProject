import django.conf
from django.contrib import messages
from django.core.mail import send_mail
import django.db.models
from django.http import HttpResponse
from django.shortcuts import redirect
import django.template.loader

from feedback.forms import FeedbackForm


def feedback(request):
    template = django.template.loader.get_template("feedback/feedback.html")
    form = FeedbackForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            send_mail(
                "Feedback",
                form.cleaned_data.get("text"),
                django.conf.settings.DJANGO_MAIL,
                [form.cleaned_data.get("mail")],
                fail_silently=False,
            )
            messages.success(request, "Данные успешно отправлены")
            return redirect("feedback:feedback")

    return HttpResponse(
        template.render(
            context,
            request,
        ),
    )


__all__ = []
