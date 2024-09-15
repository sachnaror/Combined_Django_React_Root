from django.contrib import admin
from .models import Book  # Import the Book model

admin.site.register(Book)  # Register the Book model with the admin site
