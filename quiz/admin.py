from django.contrib import admin
from .models import (
Category,
Quiz,
Question,
Option
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)

