from django.db import models
from tutors.models import TutorProfile, Subject
from users.models import User


class Lesson(models.Model):
    tutor = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f'{self.subject.name} by {self.tutor.user.username} at {self.date_time}'


class Booking(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} booked {self.lesson}'
