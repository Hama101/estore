from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image')
    
admin.site.register(Category , CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','cover','price' ,'category','mark','quantity','created_at')
admin.site.register(Product , ProductAdmin)


class MarkAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
    
admin.site.register(Mark , MarkAdmin)
