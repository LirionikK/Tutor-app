from django.db import models
from users.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    preferred_subjects = models.ManyToManyField('tutors.Subject')

    def __str__(self):
        return self.user.username
