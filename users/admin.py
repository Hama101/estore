from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user','name','avatar' , 'cover' , 'is_buyer')
    list_filter = [
            "type",
            "is_buyer",
            "created_at"
    ]
    search_fields = (
        "user__username",
        "name",
        "email",
        "phone",
        "secondPhoneNumber",
        "postcode",
    )


admin.site.register(Profile , ProfileAdmin)
