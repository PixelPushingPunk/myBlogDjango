from django.contrib import admin
from blogs.models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['title']

admin.site.register(BlogPost, BlogPostAdmin)