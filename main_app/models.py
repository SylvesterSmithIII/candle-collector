from django.db import models
from django.urls import reverse

# Create your models here.

class Candle(models.Model):
    name = models.CharField(max_length=100)
    scent = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    burn_time = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'candle_id': self.id})
