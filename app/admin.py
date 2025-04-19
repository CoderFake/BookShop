from django.contrib import admin
from .models import *
from .models import Link
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at')
    search_fields = ('title', 'url')
    list_filter = ('created_at',)