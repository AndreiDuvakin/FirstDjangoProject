import django.forms
from django.forms import ModelForm, TextInput

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
            feedback.models.Feedback.mail.field.name,
            feedback.models.Feedback.name.field.name,
        ]
        labels = {
            feedback.models.Feedback.name.field.name: "Имя отправителя",
            feedback.models.Feedback.mail.field.name: "Почта",
        }
        help_texts = {
            feedback.models.Feedback.name.field.name: "Введите имя",
            feedback.models.Feedback.mail.field.name: "Введите свою "
                                                      "электронную почту",
        }
        widgets = {
            feedback.models.Feedback.name.field.name: TextInput,
            feedback.models.Feedback.mail.field.name: TextInput,
        }
        exclude = [...]


class FeedbackImageForm(ModelForm):
    class Meta:
        model = feedback.models.FeedbackImages

        fields = [
            feedback.models.FeedbackImages.image.field.name,
        ]
        help_texts = {
            feedback.models.FeedbackImages.image.field.name: (
                'При необходимости прикрепите файл'
            ),
        }
        widgets = {
            feedback.models.FeedbackImages.image.field.name: (
                django.forms.ClearableFileInput(
                    attrs={
                        "class": "form-control",
                        "type": "image",
                    },
                )
            ),
        }


class FeedbackForm(BootstrapForm):
    class Meta:
        model = feedback.models.Feedback
        fields = [
            feedback.models.Feedback.text,
        ]
        labels = {
            feedback.models.Feedback.text: "Текст отзыва",
        }
        help_texts = {
            feedback.models.Feedback.text: "Введите текст отзыва",
        }


__all__ = []
