from rest_framework import serializers
from .models import ScannedDocument
#OcrDocument serializer
class ScannedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedDocument
        fields = ['id', 'image','created_at']