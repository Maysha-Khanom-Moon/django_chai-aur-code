from django.contrib import admin
from .models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated_at')
    search_fields = ('user__username', 'text')


admin.site.register(Tweet, TweetAdmin)