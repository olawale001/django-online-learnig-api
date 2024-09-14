from django.db import models
from users.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, related_name='courses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)    
    title = models.CharField(max_length=255)
    content = models.TextField()
    release_date = models.DateTimeField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title    
