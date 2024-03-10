import django.forms


class EchoForm(django.forms.Form):
    text = django.forms.CharField(
        widget=django.forms.TextInput(attrs={"class": "form-control"}),
        label="Текст",
        help_text="Введите текст",
    )


__all__ = []
