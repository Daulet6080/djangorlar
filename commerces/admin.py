from django.contrib import admin
from .models import Address, Order, OrderItem, OrderItemOption, PromoCode, OrderPromo

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'street')
    search_fields = ('user__email', 'city', 'street')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item_name', 'quantity', 'line_total')

@admin.register(OrderItemOption)
class OrderItemOptionAdmin(admin.ModelAdmin):
    list_display = ('order_item', 'option_name', 'price_delta')

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent')

@admin.register(OrderPromo)
class OrderPromoAdmin(admin.ModelAdmin):
    list_display = ('order', 'promo', 'applied_amount')
