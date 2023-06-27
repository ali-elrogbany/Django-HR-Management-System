from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    currentBranch = models.ForeignKey("Branches.Branch", null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name