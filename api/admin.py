from django.contrib import admin

from django.contrib import admin
from .models import Subscriber, Enrollments, Batch

admin.site.register(Subscriber)
admin.site.register(Enrollments)
admin.site.register(Batch)