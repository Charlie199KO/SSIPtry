from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(incident_model)
admin.site.register(suggestion_model)
admin.site.register(feedback_model)
admin.site.register(compliment_model)
admin.site.register(signup_model)
