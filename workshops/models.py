from django.db import models
import datetime
# Create your models here.


class Level(models.Model):
    """Workshop level model"""

    class Meta:
        """order by date"""
        ordering = ['level_name']

    level_name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=20)
   
    def __str__(self):
        """Return the level name"""
        return self.level_name
   
    def get_friendly_name(self):
        """Return the level friendly name"""
        return self.friendly_name


class Workshop(models.Model):
    """Workshops model"""

    class Meta:
        """order by date"""
        ordering = ['-date']

    name = models.CharField(max_length=50, unique=True)
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, 
        related_name='workshops'
        )
    date = models.DateField()
    start_time = models.TimeField()
    workshop_length = models.CharField(max_length=20)
    workshop_fee = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return the workshop name"""
        return self.name
