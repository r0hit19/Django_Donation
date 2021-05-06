from django.contrib import admin

# Register your models here.
from . models import homepage,donate,contact

admin.site.register(homepage)
admin.site.register(donate)
admin.site.register(contact)