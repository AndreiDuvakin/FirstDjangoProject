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
            form_text = form.cleaned_data.get("text")
            form_sender = form.cleaned_data.get("name")
            form_email = form.cleaned_data.get("mail")
            message_text = (
                f"Привет, {form_sender}\n"
                f"Мы получили твое обращение: {form_text}\n"
            )
            send_mail(
                subject="Feedback",
                message=message_text,
                from_email=django.conf.settings.DJANGO_MAIL,
                fail_silently=False,
                recipient_list=[form_email],
            )
            form.save()
            messages.success(request, "Данные успешно отправлены")
            return redirect("feedback:feedback")

    return HttpResponse(
        template.render(
            context,
            request,
        ),
    )


__all__ = []
