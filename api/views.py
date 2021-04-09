from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ScannedDocument
from .serializers import ScannedDocumentSerializer
# Create your views here.
class ListScannedDocument(APIView):
	def get(self, request, format=None):
		try:
			documents=ScannedDocument.objects.all()
			serializer=ScannedDocumentSerializer(documents,many=True)
			return Response(serializer.data)
		except Exception as e:
			print(e)
		