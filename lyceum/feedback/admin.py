from django.contrib import admin

import feedback.models


@admin.register(feedback.models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = [
        feedback.models.Feedback.status.field.name,
        feedback.models.Feedback.sender_name.field.name,
    ]
    list_display_links = [feedback.models.Feedback.status.field.name]

    def save_model(self, request, obj, form, change):
        if change:
            old_obj = feedback.models.Feedback.objects.get(pk=obj.pk)
            if obj.status != old_obj.status:
                feedback.models.StatusLog.objects.create(
                    feedback=obj,
                    user=request.user,
                    old_status=old_obj.status,
                    new_status=obj.status,
                )

        super().save_model(request, obj, form, change)
