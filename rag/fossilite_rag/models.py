from django.db import models
from pgvector.django import VectorField

# Create your models here.
class CDSDocument(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    embedding = VectorField(dimensions=1024)

    class Meta:
        db_table = 'cds_documents'  

class CollegeApplicationDocument(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    embedding = VectorField(dimensions=1024)

    class Meta:
        db_table = 'college_application_documents'  