import os
import sys
import django
import numpy as np
from pgvector.psycopg2 import register_vector


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fossilite.settings')
django.setup()


from django.db import connection

def get_college_application_rag_docs(amount, embedding):
    if not isinstance(embedding, np.ndarray):
        embedding = np.array(embedding)

    connection.ensure_connection()
    register_vector(connection.connection)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM college_application_documents
            ORDER BY embedding <-> %s
            LIMIT %s;
            """, [embedding, amount])
        return cursor.fetchall()


def get_cds_rag_docs(amount, embedding):

    if not isinstance(embedding, np.ndarray):
        embedding = np.array(embedding)

    # Register vector on Django's connection
    connection.ensure_connection()
    register_vector(connection.connection)

    with connection.cursor() as cursor:


        cursor.execute(
            """
            SELECT * FROM cds_documents
            ORDER BY embedding <-> %s
            LIMIT %s;
            """, 
            [embedding, amount])
        return cursor.fetchall()


def get_college_application_rag_docs(amount, embedding):
    pass

if __name__ == "__main__":
    embedding = np.random.rand(1024).astype(np.float32)
    amount = 10
    print(get_cds_rag_docs(amount, embedding))






