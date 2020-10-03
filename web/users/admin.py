# this file ganna show Models under Apps whichever registed in this file on admin site.
# go check localhost.8000/admin/
from django.contrib import admin
# to add "from .models import Profile" and "admin.site.register(Profile)" into admin file
# we can see the profile in the admin site.
from .models import Profile

admin.site.register(Profile)
