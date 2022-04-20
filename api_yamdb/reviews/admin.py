from django.contrib import admin
from reviews.models import Comment, Review, Title

<<<<<<< HEAD
from .models import Comment, Title, User, Review

admin.site.register(User)
=======
>>>>>>> master
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
