from django.db import models
class Movies (models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    watchlist = models.URLField(null=True, blank=True)
    poster = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title






# Create your models here.
