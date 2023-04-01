from django.contrib import admin
from .models import Event, Registration

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the admin area"

admin.site.register(Event)
admin.site.register(Registration)