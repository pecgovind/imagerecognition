from django.contrib import admin
from .models import ScannedDocument
# Register your models here.
@admin.register(ScannedDocument)
class AdminScannedDocument(admin.ModelAdmin):
    list_display=['id','image','created_at']

