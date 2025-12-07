from django.db import models
import requests

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()



def seed_database():
    LINKS = ["https://dot.ca.gov/-/media/dot-media/programs/local-assistance/documents/guide/cmrg-chapter-1-contract-management.pdf", 
            "https://www.lhc.la.gov/hubfs/Document%20Libraries/Board%20Meeting%20Archives/2023/May/LHC%20Contract%20Management%20Policy%20-%20May%202023.pdf",
            "https://des.wa.gov/sites/default/files/policy-documents/POL-DES-080-02-ContractManagementPolicy.pdf",
            "https://www.wrksolutions.com/documents/staff/contractmanagementpp/contract-management-policies-and-procedures.pdf",
            "https://sccrtc.org/wp-content/uploads/2010/09/SampleContract-Shuttle.pdf",
            "https://cpo.oc.gov/sites/cpo/files/2025-07/2024_Contract_Policy_Manual_6.24.25.pdf"]
    
    for link in LINKS:
        response = requests.get(link)
        if response.status_code == 200:
            content = response.text