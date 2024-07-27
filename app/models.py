from django.db import models


# Create your models here.


class Index(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=13)

    def __str__(self):
        return f"Ismi:{self.last_name}    Familiyasi:{self.last_name}    telefon raqami:{self.phone_number}"