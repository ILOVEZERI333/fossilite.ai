from django.db import models

# Create your models here.
class User(models.Model):
    ACADEMIC_LEVELS = {
        "MS" : "Middle School",
        "HS" : "High School",
        "CC" : "Community College",
        "UN" : "University",
    }
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    application_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=255, choices=ACADEMIC_LEVELS)
    is_active = models.BooleanField(default=True)



