from django.db import models

# Create your models here.
class ScannedDocument(models.Model):
    image= models.ImageField(upload_to ='uploads/')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'scanned_document'
