from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# class'name need always capital first letter.
# if we wanna see the profile in admin site, we need registe class Profile into admin.py in same folder.
class Profile(models.Model):
    # CASCADE means if delete User, then Profile delete too
    # but delete Profile won't delete User.
    # 'user' and 'image' are what we call field.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # django wil automatically create a floder which name is "profile_pics" for upload_to.
    # also can be added into other folder, see settings.py MEDIA_ROOT.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

    # this function use to printout a username plus 'Profile'
    # e.g. if a user's name is Jun, it'll show 'Jun Profile'.
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # this ganna use Image function which import from pillow
        # to open current instance image and save to img.
        img = Image.open(self.image.path)
        # if img pixal bigger than 300, triming into 300*300.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300) # tuple
            img.thumbnail(output_size) # resize img
            img.save(self.image.path) # save
