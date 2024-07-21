from django.db import models
from users.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    subjects = models.ManyToManyField(Subject)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.JSONField()

    def __str__(self):
        return self.user.username
