import string

import django.core.exceptions
import django.utils.deconstruct


@django.utils.deconstruct.deconstructible
class ValidateMustContain:
    def __init__(self, *words):
        self.words = [word.lower() for word in words]

    def __call__(self, value):
        for i in string.punctuation + "©":
            value = value.replace(i, " ")
        value = value.lower().split()
        for word in self.words:
            if word in value:
                return
        raise django.core.exceptions.ValidationError(
            "Значение должно содержать слово превосходно или роскошно",
        )


__all__ = []
