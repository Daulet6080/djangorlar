from django.core.management.base import BaseCommand
from catalogs.models import Restaurant, Category, Option, MenuItem, ItemCategory, ItemOption
from commerces.models import Address, Order, OrderItem, OrderItemOption, PromoCode, OrderPromo
from django.contrib.auth.models import User
from faker import Faker
import random
from decimal import Decimal

fake = Faker()

class Command(BaseCommand):
    help = "Generate 20 test records for each model."

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("🚀 Starting test data generation..."))

        # Users
        for _ in range(5):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="test1234"
            )

        # Restaurants
        restaurants = [Restaurant.objects.create(name=fake.company(), description=fake.text()) for _ in range(10)]

        # Categories
        categories = [Category.objects.create(name=fake.word()) for _ in range(10)]

        # Options
        options = [Option.objects.create(name=fake.word()) for _ in range(10)]

        # Menu Items
        items = []
        for _ in range(20):
            item = MenuItem.objects.create(
                restaurant=random.choice(restaurants),
                name=fake.word(),
                description=fake.text(),
                base_price=Decimal(random.uniform(5, 50)).quantize(Decimal("0.01")),
                is_available=True
            )
            items.append(item)

        # ItemCategory
        for item in items:
            ItemCategory.objects.create(item=item, category=random.choice(categories))

        # ItemOption
        for item in items:
            ItemOption.objects.create(
                item=item,
                option=random.choice(options),
                price_delta=Decimal(random.uniform(0, 10)).quantize(Decimal("0.01")),
                is_default=False
            )

        # Addresses
        users = list(User.objects.all())
        addresses = [
            Address.objects.create(user=random.choice(users), street=fake.street_address(), city=fake.city())
            for _ in range(20)
        ]

        # Promo codes
        promos = [PromoCode.objects.create(code=fake.lexify(text="PROMO????"), discount_percent=10) for _ in range(5)]

        # Orders
        for _ in range(20):
            order = Order.objects.create(
                user=random.choice(users),
                restaurant=random.choice(restaurants),
                address=random.choice(addresses),
                status=random.choice(["new", "confirmed", "delivering", "done"]),
                subtotal=Decimal(random.uniform(20, 200)).quantize(Decimal("0.01")),
                discount_total=Decimal(random.uniform(0, 20)).quantize(Decimal("0.01")),
                total=Decimal(random.uniform(20, 250)).quantize(Decimal("0.01")),
            )

            # Items in order
            for _ in range(random.randint(1, 5)):
                item = random.choice(items)
                order_item = OrderItem.objects.create(
                    order=order,
                    item_name=item.name,
                    item_price=item.base_price,
                    quantity=random.randint(1, 3),
                    line_total=item.base_price * Decimal(random.randint(1, 3)),
                )

                # Options for order items
                for _ in range(random.randint(0, 2)):
                    OrderItemOption.objects.create(
                        order_item=order_item,
                        option_name=random.choice(options).name,
                        price_delta=Decimal(random.uniform(0, 5)).quantize(Decimal("0.01")),
                    )

            # Promo codes applied
            if random.random() < 0.5:
                promo = random.choice(promos)
                OrderPromo.objects.create(order=order, promo=promo, applied_amount=Decimal("5.00"))

        self.stdout.write(self.style.SUCCESS("✅ Successfully generated test data!"))
