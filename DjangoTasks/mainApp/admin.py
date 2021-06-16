from django.contrib import admin

from .models import FeedItem, RegisteredUser

admin.site.register(FeedItem)
admin.site.register(RegisteredUser)
