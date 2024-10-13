from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uuid = models.UUIDField(primary_key=True)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)
    collection = models.ForeignKey(Collection, related_name='movies', on_delete=models.CASCADE)
