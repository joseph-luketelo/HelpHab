from django.contrib import admin
from .models import Subscriber, QuestionsTable, Room, Message

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'user_rec', 'date_time')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('label', 'name')

admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
admin.site.register(Subscriber)
admin.site.register(QuestionsTable, QuestionsAdmin)