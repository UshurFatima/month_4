from django.db import models


class ManasFilm(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='parser/')
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title
