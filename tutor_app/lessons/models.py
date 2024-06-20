from django.db import models


class User(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('tutor', 'Tutor'),
    ]
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_role = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)


class TutorCourse(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_role': 'tutor'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)


class Schedule(models.Model):
    DAY_OF_WEEK_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    tutor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_role': 'tutor'})
    day_of_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    student = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE,
                                limit_choices_to={'user_role': 'student'})
    tutor = models.ForeignKey(User, related_name='tutor_bookings', on_delete=models.CASCADE,
                              limit_choices_to={'user_role': 'tutor'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES)
