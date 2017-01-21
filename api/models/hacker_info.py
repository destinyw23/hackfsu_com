from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from api.models import Hackathon, School


class HackerInfo(models.Model):
    SCHOOL_YEAR_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior')
    )

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(to=Hackathon, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False, blank=True)
    comments = models.CharField(max_length=1000, default='', blank=True)
    misc_info = JSONField(default=None, null=True, blank=True)

    is_first_hackathon = models.BooleanField()
    is_adult = models.BooleanField()
    school = models.ForeignKey(to=School, on_delete=models.SET_NULL, null=True)
    school_year = models.CharField(max_length=2, choices=SCHOOL_YEAR_CHOICES)
    school_major = models.CharField(max_length=100)
    resume_file_name = models.CharField(max_length=300, default='', blank=True)

    rsvp = models.BooleanField(default=False, blank=True)
    checked_in = models.BooleanField(default=False, blank=True)
