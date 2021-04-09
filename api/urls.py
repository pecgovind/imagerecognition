from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('documents/',views.ListScannedDocument.as_view(), name='documents'),
]
