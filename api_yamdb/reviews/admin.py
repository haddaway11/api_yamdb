from django.contrib import admin

from .models import Title, User, Comment, Review

admin.site.register(User)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
