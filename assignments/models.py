from django.db import models
from cources.models import Course
from users.models import CustomUser

class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='submission', on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_on = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.student.username} - {self.assignment.title}'
