import django.contrib.admin
from django.contrib import admin

import feedback.models


class FeedbackAuther(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackAuther
    fields = [
        feedback.models.FeedbackAuther.name.fields.name,
        feedback.models.FeedbackAuther.mail.fields.name,
    ]
    can_delete = False


class FeedbackImages(django.contrib.admin.TabularInline):
    model = feedback.models.FeedbackImages
    fields = [
        feedback.models.FeedbackImages.field.name,
    ]


@admin.register(feedback.models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        feedback.models.Feedback.status.field.name,
        feedback.models.Feedback.text.field.name,
    ]
    inlines = [
        FeedbackImages,
        FeedbackAuther,
    ]

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = feedback.models.Feedback.objects.get(pk=obj.pk)
            if obj.status != old_obj.status:
                feedback.models.StatusLog.objects.create(
                    feedback=obj,
                    user=request.user,
                    _from=old_obj.status,
                    to=obj.status,
                )

        super().save_model(request, obj, form, change)


__all__ = []
