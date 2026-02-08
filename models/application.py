from django.db import models
from pgvector.django import VectorField


class ApplicationDocument(models.Model):
    id = models.AutoField(primary_key=True)
    application_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    content = models.TextField()
    embedding = VectorField(dimensions=1024)

    class Meta:
        db_table = 'college_application_documents'


