from django.db import models
from pgvector.django import VectorField


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    larger_document_name = models.CharField(max_length=200)
    content = models.TextField()
    embedding = VectorField(dimensions=1024)

    class Meta:
        db_table = 'documents'