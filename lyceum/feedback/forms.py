from django.forms import ModelForm, TextInput

import feedback.models


class FeedbackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = feedback.models.Feedback
        fields = [
            feedback.models.Feedback.text.field.name,
            feedback.models.Feedback.mail.field.name,
            feedback.models.Feedback.name.field.name,
        ]
        labels = {
            feedback.models.Feedback.name.field.name: "Имя отправителя",
            feedback.models.Feedback.text.field.name: "Текст",
            feedback.models.Feedback.mail.field.name: "Почта",
        }
        help_texts = {
            feedback.models.Feedback.name.field.name: "Введите имя",
            feedback.models.Feedback.text.field.name: "Введите отзыв",
            feedback.models.Feedback.mail.field.name: "Введите свою "
            "электронную почту",
        }
        widgets = {
            feedback.models.Feedback.name.field.name: TextInput,
            feedback.models.Feedback.text.field.name: TextInput,
            feedback.models.Feedback.mail.field.name: TextInput,
        }
        exclude = [...]


__all__ = []
