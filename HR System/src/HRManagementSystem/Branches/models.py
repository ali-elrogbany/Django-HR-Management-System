from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)
    buildingNumber = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    manager = models.ForeignKey("Employees.Employee", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name