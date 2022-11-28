from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse_lazy

class Hero(models.Model):
    name = models.CharField(max_length=200, default='name')
    strengths = models.TextField(max_length=500, default='strengths')
    weaknesses = models.TextField(max_length=500, default='weaknesses')
    identity = models.TextField(max_length=200, default='identity')
    description = models.TextField(max_length=2000, default='description')
    notes = models.TextField(max_length=2000, default='notes')
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('hero_list')

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'


class Photo (models.Model):

    hero = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])