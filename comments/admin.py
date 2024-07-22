from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title',  'status','user_id','post_id')
    list_filter = ('status',)
    search_fields = ('title', 'comments', 'user__username', 'post__title')

admin.site.register(Comment, CommentAdmin)

# admin.site.register(Comment)


# Register your models here.
