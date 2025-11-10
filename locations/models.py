from django.db import models

# Create your models here.
class Accommodations(models.Model):
    ACCOMMODATION_TYPES = [
        ('hotel', 'Hotel'),
        ('resort', 'Resort'),
        ('restaurant', 'Restaurant'),
        ('lodge', 'Lodge'),
    ]

    name = models.CharField(max_length=100, primary_key=True)
    province = models.CharField(max_length=50)
    town = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=ACCOMMODATION_TYPES,
        default='hotel'
    )
    
    img_url = models.ImageField(upload_to='locations/images/', blank=True, null=True)

    
    def __str__(self):
        return self.name
    