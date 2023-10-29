from django.contrib import admin
from .models import Post
admin.site.site_header = "CookWithIt Admin"
admin.site.site_title = "CookWithIt Administration"
admin.site.index_title = "CookWithIt Dashboard"
admin.site.register(Post)
