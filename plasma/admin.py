from django.contrib import admin

# Register your models here.
from .models import Donor,Blood

admin.site.register(Donor)
admin.site.register(Blood)
