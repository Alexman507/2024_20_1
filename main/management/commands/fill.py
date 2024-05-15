import json

from django.core.management import BaseCommand
from django.db import connection

from main.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories = []
        # Здесь мы получаем данные из фикстур с категориями
        with open('main/data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.category":
                    categories.append(item)
        return categories

    @staticmethod
    def json_read_products():
        products = []
        # Здесь мы получаем данные из фикстур с продуктами
        with open('main/data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.product":
                    products.append(item)
        return products

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE main_category RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_product RESTART IDENTITY CASCADE;")
        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_list = []
        product_for_create = []
        category_list = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_list.append(
                Category(
                    pk=category['pk'], name=category['fields']['name'],
                    description=category['fields']['description']
                )
            )

        for category_item in category_list:
            print(category_list)
            category_for_create.append(
                Category.objects.create(category_item)
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_list.append(
                Product(pk=product['pk'], name=product['fields']['name'],
                        description=product['fields']['description'],
                        price=product['fields']['price'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        preview=product['fields']['preview'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']))

        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(product_item)
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
