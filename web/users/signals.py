"""
this file need imported by apps.py.
"""

# when user create a account, post_save send a signal by sender function User
# to a receiver fucntion.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# @receiver(post_save, sender=User) means when User condition is saved and method is
# post ,send this signel to receiver which is create_profile function
# it takes all the parameters that post_save passed.
@receiver(post_save, sender=User)
# **kwargs means it'll take any addtional keyword argument until the fucntion finshed.
def create_profile(sender, instance, created, **kwargs):
    # if user is created, also create a profile with same user's instance.
    if created:
        Profile.objects.create(user=instance)


# this means when User post_save, save the user's profile too.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
