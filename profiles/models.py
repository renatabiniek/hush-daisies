"""Models for Profiles app"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from workshops.models import Workshop


class UserProfile(models.Model):
    """
    User profile extending django User model.
    Allows users to save personal info and view order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
        )
    default_house_number_or_name = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_street_address_1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_street_address_2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
        )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
        )
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
        )

    def __str__(self):
        """Return username"""
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Each time user object is saved, instance of UserProfile
    gets created or existing profile updated.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class WorkshopFavourites(models.Model):
    """
    Workshop favourites model. Allows a logged in user to save a workshop
    to a list of favourites in their user profile.
    """
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    workshop = models.ManyToManyField(
        Workshop, blank=True, related_name="workshop_favourites"
        )

    def __str__(self):
        """Return workshops added to favourites for the user"""
        return self.user.user.username
