from django.db import models

# Create your models here.
class Profiles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255, unique=True, default="")
    is_verified = models.BooleanField(max_length=10,default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
