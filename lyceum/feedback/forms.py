import django.forms
from django.forms import TextInput

import feedback.models


class BootstrapForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class FeedbackAutherForm(BootstrapForm):
    class Meta:
        model = feedback.models.FeedbackAuther
        fields = [
            feedback.models.FeedbackAuther.mail.field.name,
            feedback.models.FeedbackAuther.name.field.name,
        ]
        labels = {
            feedback.models.FeedbackAuther.name.field.name: "Имя отправителя",
            feedback.models.FeedbackAuther.mail.field.name: "Почта",
        }
        help_texts = {
            feedback.models.FeedbackAuther.name.field.name: "Введите имя",
            feedback.models.FeedbackAuther.mail.field.name: "Введите свою "
            "электронную почту",
        }
        widgets = {
            feedback.models.FeedbackAuther.name.field.name: TextInput,
            feedback.models.FeedbackAuther.mail.field.name: TextInput,
        }
        exclude = [...]


class FeedbackImageForm(BootstrapForm):
    class Meta:
        model = feedback.models.FeedbackImages

        fields = [
            feedback.models.FeedbackImages.image.field.name,
        ]
        help_texts = {
            feedback.models.FeedbackImages.image.field.name: (
                "При необходимости прикрепите файл"
            ),
        }
        widgets = {
            feedback.models.FeedbackImages.image.field.name: (
                django.forms.FileInput(
                    attrs={
                        "multiple": True,
                    },
                )
            ),
        }


class FeedbackForm(BootstrapForm):
    class Meta:
        model = feedback.models.Feedback
        fields = [
            feedback.models.Feedback.text.field.name,
        ]
        labels = {
            feedback.models.Feedback.text.field.name: "Текст отзыва",
        }
        help_texts = {
            feedback.models.Feedback.text.field.name: "Введите текст отзыва",
        }


__all__ = []
