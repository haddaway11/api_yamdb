from django.contrib import admin
from reviews.models import Comment, Review, Title

admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
