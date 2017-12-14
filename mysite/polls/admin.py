from django.contrib import admin

# Register your models here.
# password: abc123456789

from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)
