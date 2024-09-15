# Django_App/management/commands/create_fake_books.py
from django.core.management.base import BaseCommand
from Django_App.models import Book
from faker import Faker


class Command(BaseCommand):
    help = 'Create fake book records'

    def handle(self, *args, **kwargs):
        fake = Faker()
        books = []

        for _ in range(10):  # Create 10 fake books
            books.append(Book(
                name=fake.catch_phrase(),  # Generate a fake book title
                author=fake.name(),  # Generate a fake author name
                published_date=fake.date_between(start_date='-10y', end_date='today'),  # Random date in the last 10 years
                isbn=fake.isbn13(),  # Generate a fake ISBN
                summary=fake.text(max_nb_chars=200)  # Generate a short summary
            ))

        # Bulk create the books
        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake book records!'))
