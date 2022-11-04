from django.db import models
import datetime
from django.contrib.auth.models import User
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
        ordering = ['date']

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


class WorkshopTestimonial(models.Model):
    """Testimonials for workshops model"""
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='testimonials')
    workshop = models.ForeignKey(
        Workshop, on_delete=models.CASCADE,
        related_name='workshop_testimonials'
        )
    testimonial_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        """Order testimonials by date added in ascending order"""
        ordering = ['date_added']

    def __str__(self):
        return f"{self.reviewer} wrote on {self.date_added}"
