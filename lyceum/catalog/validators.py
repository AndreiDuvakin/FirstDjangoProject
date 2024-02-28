import django.core.exceptions
import django.utils.deconstruct


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *words):
        self.words = [word.lower() for word in words]

    def __call__(self, value):
        value = value.lower().split()
        for word in self.words:
            if word in value:
                return
        raise django.core.exceptions.ValidationError(
            "Значение должно содержать слово превосходно или роскошно",
        )


__all__ = [
    ValidateMustContain,
]
