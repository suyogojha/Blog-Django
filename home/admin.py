from django.contrib import admin

# Register your models here.
from .models import BlogModel , Profile



@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "slug", "user"]





@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "is_verified", "token"]


