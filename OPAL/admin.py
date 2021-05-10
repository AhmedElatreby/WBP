from django.contrib import admin
from . import models

admin.site.register(models.Team)
admin.site.register(models.Therapist)
admin.site.register(models.Patient)
admin.site.register(models.DirectInput)
admin.site.register(models.IndirectInput)
admin.site.register(models.Therapy)
