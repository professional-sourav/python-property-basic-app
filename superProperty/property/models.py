from django.db import models

class PropertyType(models.TextChoices):
    APPARTMENT = 'Appartment'
    HOSTEL = 'Hostel'
    HOUSE = 'House'

# Create your models here.
class Property(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.APPARTMENT,
    )
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='attachments')
    uploaded_at = models.DateTimeField(auto_now_add=True)
