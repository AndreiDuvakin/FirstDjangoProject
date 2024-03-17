import django.conf
from django.contrib import messages
from django.core.mail import send_mail
import django.db.models
from django.http import HttpResponse
from django.shortcuts import redirect
import django.template.loader

from feedback.forms import FeedbackForm, FeedbackAutherForm, FeedbackImageForm
from feedback.models import Feedback, FeedbackAuther, FeedbackImages


def feedback(request):
    template = django.template.loader.get_template("feedback/feedback.html")
    feedback_form = FeedbackForm(request.POST or None)
    feedback_auther = FeedbackAutherForm(request.POST or None)
    feedback_images = FeedbackImageForm(request.POST or None)
    context = {
        "feedback_form": feedback_form,
        "feedback_auther": feedback_auther,
        "feedback_images": feedback_images,
    }
    forms = [
        feedback_form,
        feedback_images,
        feedback_auther,
    ]
    if request.method == "POST" and all(form.is_valid() for form in forms):
        form_text = feedback_form.cleaned_data.get("text")
        form_sender = feedback_auther.cleaned_data.get("name")
        form_email = feedback_auther.cleaned_data.get("mail")
        message_text = (
            f"Привет, {form_sender}\n"
            f"Мы получили твое обращение: {form_text}\n"
        )
        send_mail(
            subject="Feedback",
            message=message_text,
            from_email=django.conf.settings.DJANGO_MAIL,
            fail_silently=True,
            recipient_list=[form_email],
        )
        feedback_item = Feedback.objects.create(
            **feedback_form.cleaned_data,
        )
        feedback_item.save()
        FeedbackAuther.objects.create(
            feedback=feedback_item,
            **feedback_auther.cleaned_data,
        )
        for image in request.FILES.getlist(
            FeedbackImages.image.field.name,
        ):
            FeedbackImages.objects.create(
                image=image,
                feedback=feedback_item,
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
