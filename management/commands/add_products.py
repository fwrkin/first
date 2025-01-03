from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, null=None, *args, **options):
        category, _ = Category.objects.get_or_create(name='Овощи')

        products = [
            {'name': 'Помидор', 'description': null, 'price': '10.0', 'category': category},
            {'name': 'Огурец', 'description': null, 'price': '15,0', 'category': category}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))