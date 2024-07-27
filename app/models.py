from django.db import models


# Create your models here.


class Index(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=13)

    def __str__(self):
        return self.first_name