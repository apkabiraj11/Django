from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=20)

    def __str__(self):
        return f"ID: {self.id} - {self.name}"
