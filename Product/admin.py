from django.contrib import admin
from .models import elastic, thread, velcro
# Register your models here.

admin.site.register(elastic)
admin.site.register(velcro)
admin.site.register(thread)