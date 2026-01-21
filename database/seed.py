from django.db import models
import requests

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()



def seed_database():
    IVY_LINKS = ["https://bpb-us-e1.wpmucdn.com/sites.harvard.edu/dist/6/210/files/2025/06/HarvardUniversity_CDS_2024-2025.pdf", 
            "https://upenn.app.box.com/s/ckv4frz37rzxa4u6bdiv2h4yzykqm4ef",
            "https://opir.columbia.edu/sites/opir.columbia.edu/files/content/Common%20Data%20Set/2024-25_Columbia_General_Studies_CDS.pdf",
            "https://www.dartmouth.edu/oir/pdfs/cds_2024-2025.pdf",
            "https://oir.yale.edu/sites/default/files/yale_cds_2024-25_rmd_20250612.pdf",
            "https://irp.dpb.cornell.edu/wp-content/uploads/2025/07/CDS-2024-2025-v6-print.pdf",
            "https://oir.brown.edu/sites/default/files/2020-04/CDS_2024_2025.pdf",
            "https://ir.princeton.edu/sites/g/files/toruqf2041/files/documents/CDS_2425_Princeton_v2.pdf"]
    
    UC_LINKS = ["https://apb.ucla.edu/file/b099e788-a3fc-4395-8842-29db4ff42da3",
    "https://bpb-us-e2.wpmucdn.com/sites.uci.edu/dist/2/5478/files/2025/09/CDS-2024-25.pdf",
    "https://ir.ucsd.edu/stats/undergrad/CDS_2024-2025_Final1.pdf",
    "https://aggiedata.ucdavis.edu/sites/g/files/dgvnsk1841/files/media/documents/CDS_UCD.pdf",
    "https://ir.ucr.edu/sites/default/files/2025-04/cds-2024-2025.pdf",
    "https://mediafiles.ucsc.edu/iraps/common-data-set/common-data-set-2024-25.pdf",
    "https://oir.usc.edu/wp-content/uploads/sites/3/2025/10/CDS_2024-2025_FINAL-3.pdf"
    ]

    for link in IVY_LINKS:
        response = requests.get(link)
        if response.status_code == 200:
            content = response.text