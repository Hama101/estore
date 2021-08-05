from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image')
    
admin.site.register(Category , CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','cover','price' ,'category','mark','quantity','created_at')
    list_filter = [
            "category",
            "mark",
            "created_at"
    ]
    search_fields = (
        "category__title",
        "mark__name",
        "name",
        "quantity",
        "SKU",
        "price",
    )
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        try:
            min_price, max_price = search_term.split('-')
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(price__gte=min_price, price__lte=max_price)
            queryset |= self.model.objects.filter(quantity__gte=min_price, quantity__lte=max_price)
        return queryset, use_distinct


admin.site.register(Product , ProductAdmin)


class MarkAdmin(admin.ModelAdmin):
    list_display = ('name' ,)
    
admin.site.register(Mark , MarkAdmin)
