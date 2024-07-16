from django.db import models
from django.core.validators import FileExtensionValidator 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='media/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV', 'jpg', 'png'])
    ])

    def __str__(self) -> str:
        return self.title


    
class Comment(models.Model):
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class LikeVideo(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    video_model = models.ForeignKey(Lesson,on_delete=models.SET_NULL,null=True)
    like_or_dislike = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)