from django.db import models

class Level(models.Choices):
    MIDDLE_SCHOOL = 'MIDDLE_SCHOOL'
    HIGHSCHOOL = 'HIGHSCHOOL'
    COMMUNITY_COLLEGE = 'COMMUNITY_COLLEGE'

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharFieldField(max_length=255)
    application_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=255, choices=Level.choices)
    is_active = models.BooleanField(default=True)