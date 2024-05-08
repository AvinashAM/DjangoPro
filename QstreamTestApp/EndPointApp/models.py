from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    country = models.CharField(max_length=100, blank=True)