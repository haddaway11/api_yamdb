from django.contrib import admin

from .models import Comment, Title, User, Review

admin.site.register(User)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
