from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    first_name = models.CharField(max_length=50, blank=True, default="")
    last_name = models.CharField(max_length=50, blank=True, default="")
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number