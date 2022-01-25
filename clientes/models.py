from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bio = models.TextField(blank = True)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name


