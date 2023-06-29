from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    age = models.IntegerField()
    start_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name