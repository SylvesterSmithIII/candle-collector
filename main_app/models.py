from django.db import models
from django.urls import reverse

# Create your models here.

class Wax(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("wax_detail", kwargs={"pk": self.id})

class Candle(models.Model):
    name = models.CharField(max_length=100)
    scent = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    burn_time = models.IntegerField()
    waxs = models.ManyToManyField(Wax)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'candle_id': self.id})
    

class Store(models.Model):
    name = models.CharField(max_length=100)
    carries = models.BooleanField(default=True)

    candle = models.ForeignKey(Candle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}? {self.carries}"
