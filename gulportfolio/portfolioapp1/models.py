from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(max_length=200, verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name+"-"+self.email