from django.contrib import admin
from .models import RawMaterial, MaterialUnit, Account, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'created_at', 'get_total_items')
    list_filter = ('created_at',)
    
    def get_total_items(self, obj):
        return obj.items.count()
    get_total_items.short_description = 'Total Items'

admin.site.register(RawMaterial)
admin.site.register(MaterialUnit)
admin.site.register(Account)
admin.site.register(Product)
admin.site.register(OrderItem)

