from django.db import models
from django.core.validators import MinValueValidator
from abstracts.models import AbstractSoftDeletableModel  # ✅ импортируем абстрактную модель


class Restaurant(AbstractSoftDeletableModel):  # ✅ наследуем
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(AbstractSoftDeletableModel):  # ✅ наследуем
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(AbstractSoftDeletableModel):  # ✅ наследуем
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(AbstractSoftDeletableModel):  # ✅ наследуем
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ItemCategory(AbstractSoftDeletableModel):  # ✅ наследуем
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('item', 'category')


class ItemOption(AbstractSoftDeletableModel):  # ✅ наследуем
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    price_delta = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    is_default = models.BooleanField(default=False)

    class Meta:
        unique_together = ('item', 'option')
