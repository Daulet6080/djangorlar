from django.contrib import admin
from .models import Address, Order, OrderItem, OrderItemOption, PromoCode, OrderPromo


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "city", "street")
    search_fields = ("city", "street", "user__username")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "restaurant", "status", "total", "created_at")
    list_filter = ("status", "restaurant")
    search_fields = ("user__username",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "item_name", "quantity", "line_total")


@admin.register(OrderItemOption)
class OrderItemOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "order_item", "option_name", "price_delta")


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "discount_percent")
    search_fields = ("code",)


@admin.register(OrderPromo)
class OrderPromoAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "promo", "applied_amount")
