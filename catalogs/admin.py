from django.contrib import admin
from .models import Restaurant, MenuItem, Category, ItemCategory, Option, ItemOption


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "restaurant", "base_price", "is_available")
    list_filter = ("restaurant", "is_available")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "category", "position")
    list_filter = ("category",)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(ItemOption)
class ItemOptionAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "option", "price_delta", "is_default")
    list_filter = ("is_default",)
