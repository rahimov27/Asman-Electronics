from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('index', kwargs={'client_id': self.pk})

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone}"

    class Meta:
        db_table = "Клиенты"
        