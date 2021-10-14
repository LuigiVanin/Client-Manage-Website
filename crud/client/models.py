from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    published = models.BooleanField(default=True)
    debt = models.FloatField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name