from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from abstracts.models import AbstractSoftDeletableModel  # ✅ импортируем

class Address(AbstractSoftDeletableModel):  # ✅ наследуем
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.city}, {self.street}"


class Order(AbstractSoftDeletableModel):  # ✅ наследуем
    STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('delivering', 'Delivering'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey('catalogs.Restaurant', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"


class OrderItem(AbstractSoftDeletableModel):  # ✅ наследуем
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    line_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.item_name} x {self.quantity}"


class OrderItemOption(AbstractSoftDeletableModel):  # ✅ наследуем
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='options')
    option_name = models.CharField(max_length=100)
    price_delta = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class PromoCode(AbstractSoftDeletableModel):  # ✅ наследуем
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.code


class OrderPromo(AbstractSoftDeletableModel):  # ✅ наследуем
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    promo = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    applied_amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('order', 'promo')
