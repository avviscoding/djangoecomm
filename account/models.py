from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.user)
