from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    release_year = models.IntegerField()
    genre1 = models.CharField(max_length = 30)
    genre2 = models.CharField(max_length = 30)
    genre3 = models.CharField(max_length = 30)
    image = models.ImageField()

    def __str__(self):
        return self.title
