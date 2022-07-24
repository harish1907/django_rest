from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Students"
        
    def __str__(self):
        return self.name
    