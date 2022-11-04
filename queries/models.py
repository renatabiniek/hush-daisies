from django.db import models

# Create your models here.


class CustomRequest(models.Model):
    """Custom requests and queries model"""
    QUOTE = 'QUOTE'
    QUESTION = 'QUESTION'
    RESERVATION = 'RESERVATION'
    QUERY_CHOICES = [
        (QUOTE, 'Get a quote for a custom order'),
        (QUESTION, 'Ask a question'),
        (RESERVATION, 'Save your spot'),
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    request_type = models.CharField(
        max_length=30,
        choices=QUERY_CHOICES,
        default=QUESTION
        )
    reference_link = models.URLField(max_length=200, blank=True)
    request_body = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return customer name"""
        return self.name
