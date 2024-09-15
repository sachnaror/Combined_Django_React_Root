from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.author}"

    class Meta:
        ordering = ['name']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
