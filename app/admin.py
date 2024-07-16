from django.contrib import admin
from .models import Comment,Course,User,Lesson,Video

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)