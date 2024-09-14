from django.db import models
from users.models import CustomUser
from cources.models import Course

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_amount_intent = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.amount}'