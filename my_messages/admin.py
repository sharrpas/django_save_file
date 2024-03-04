from django.contrib import admin

# Register your models here.
from .models import MyMessages
admin.site.register(MyMessages)