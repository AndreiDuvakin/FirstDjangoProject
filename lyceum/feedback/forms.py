import django.forms

import feedback.models


class FeedbackForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = feedback.models.Feedback
        fields = [
            feedback.models.Feedback.text.field.name,
            feedback.models.Feedback.mail.field.name,
        ]
        labels = {
            feedback.models.Feedback.text.field.name: "Текст",
            feedback.models.Feedback.mail.field.name: "Почта",
        }
        help_texts = {
            feedback.models.Feedback.text.field.name: "Введите отзыв",
            feedback.models.Feedback.mail.field.name: "Введите свою "
            "электронную почту",
        }
        exclude = [...]


__all__ = []
