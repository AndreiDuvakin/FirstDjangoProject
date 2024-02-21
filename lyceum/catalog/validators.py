import django.core.exceptions
import django.utils.deconstruct


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *words):
        self.words = [word.lower() for word in words]

    def __call__(self, value):
        value = value.lower()
        for word in self.words:
            if word not in value:
                raise django.core.exceptions.ValidationError(
                    f"Значение должно содержать слово '{word}'",
                )
