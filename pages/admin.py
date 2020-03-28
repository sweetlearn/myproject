from django.contrib import admin
from .models import Customer, Generator, SubLine

admin.site.register(Customer)
admin.site.register(Generator)
admin.site.register(SubLine)
