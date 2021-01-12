"""
Definition of urls for 412Connect
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from p412connect import views


urlpatterns = [
    path('', views.home, name='412connect/'),
    path('contact/', views.contact, name='412connect/contact'),
    path('about/', views.about, name='412connect/about'),
    path('directory/', views.directory, name='412connect/directory'),
    path('dashboard/', views.dashboard, name='412connect/dashboard'),
    path('submitreview/', views.submitreview, name='412connect/submitreview'),
]
