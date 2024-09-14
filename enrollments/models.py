from django.db import models
from users.models import CustomUser
from cources.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.title}'
