import email
from turtle import title
from django.core.mail import send_mail
from django.utils import timezone
from cources.models import Lesson, CustomUser

def notify_users_of_new_lessons():
    lessons = Lesson.objects.filter(release_date_lte=timezone.now(), notified=False)

    for lesson in lessons:
        students = CustomUser.objects.filter(course=lesson.course)
        for student in students:
            send_mail(
                subject=f'New Lesson Available: {lesson.title}',
                message=f'The new lesson "{lesson.title}" is now availabe in the course {lesson.course.title}',
                from_email='olacodeire@gmail.com',
                recipient_list=[student.email]
            )
        lesson.notified = True
        lesson.save()    