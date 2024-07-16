from django.contrib import admin
from .models import Comment,Course,User,Lesson

class AdminCourse(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name',)
    search_fields = ('name',)


class AdminLesson(admin.ModelAdmin):
    list_display = ('title', 'created', 'course')
    list_display_links = ('title',)
    list_editable = ('course',)
    list_filter = ('course',)
    search_fields = ('title',)




admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Course,AdminCourse)
admin.site.register(Lesson,AdminLesson)