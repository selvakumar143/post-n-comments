from django.contrib import admin
from .models import BlogPost


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug')
        }),
        ('Description', {
            'fields': ('short_description', 'content')
        }),
         ('Advanced Information', {
            'fields': ('media','status', 'author')
        })         
    )
    list_display = ('title','slug', 'status','author')
    list_filter = ('status',)
    search_fields = ('title', 'content')

admin.site.register(BlogPost, PostAdmin)