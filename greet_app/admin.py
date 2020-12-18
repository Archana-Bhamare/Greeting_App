from django.contrib import admin

# Register your models here.
from greet_app.models import Person

admin.site.register(Person)
