from django.contrib import admin
from . import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title","time")

# Register your models here.
admin.site.register(models.BlogPost,BlogPostAdmin)