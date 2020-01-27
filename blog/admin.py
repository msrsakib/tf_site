from django.contrib import admin
from .models import Post, Comment

# Registered model
admin.site.register(Post)
admin.site.register(Comment)
