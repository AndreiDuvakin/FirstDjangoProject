import django.contrib.auth
import django.forms

import users.models


class BootstrapForm(django.forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class SignUpForm(django.contrib.auth.forms.UserCreationForm, BootstrapForm):
    class Meta(django.contrib.auth.forms.UserCreationForm.Meta):
        fields = ("email", "username")


class CustomUserChangeForm(
    django.contrib.auth.forms.UserChangeForm,
    BootstrapForm,
):
    class Meta(django.contrib.auth.forms.UserChangeForm.Meta):
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
        )


class ProfileForm(django.forms.ModelForm):
    class Meta:
        model = users.models.Profile
        fields = [
            model.birthday.field.name,
            model.image.field.name,
            model.coffe_count.field.name,
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["coffe_count"].widget.attrs["readonly"] = True
        self.fields["coffe_count"].widget.attrs["disabled"] = True
        self.fields["birthday"].widget = django.forms.SelectDateWidget()

        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


def set_custom_form(form):
    class CustomForm(form, BootstrapForm):
        pass

    return CustomForm


__all__ = []
