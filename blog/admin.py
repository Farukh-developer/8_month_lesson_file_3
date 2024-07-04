from django.contrib import admin

# Register your models here.
from .models import Area, Construction_organization, Construction_building


admin.site.register([Area, Construction_organization, Construction_building])
