from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from admin_interface.models import Theme

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Theme)

admin.site.register(MetaTags)
