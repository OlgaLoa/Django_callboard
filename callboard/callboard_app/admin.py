from django.contrib import admin
# для загрузки изобр через админ панель
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',) #только поле модели Post где будет возможна загрузка изобр.

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
