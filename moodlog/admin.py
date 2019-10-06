from django.contrib import admin
from moodlog.models import Mood, Action, MoodLog


class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'mood', 'action', 'timestamp')
    list_editable = ('mood', 'action')
    search_fields = ('user',)
    list_filter = ('mood', 'action')


admin.site.register(Mood)
admin.site.register(Action)
admin.site.register(MoodLog, MoodLogAdmin)
