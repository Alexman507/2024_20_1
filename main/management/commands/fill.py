import json

from django.core.management import BaseCommand
from main.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('data/main_data.json', encoding='utf-8') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        Product.truncate_table_restart_id()

        # Удалите все категории
        Category.objects.all().delete()
        Category.truncate_table_restart_id()

        # Создайте списки для хранения объектов
        product_list = []
        product_for_create = []
        category_list = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_data():
            if category["model"] == "main.category":
                category_list.append(
                    Category(
                        {"id": category['pk'], "name": category['fields']['name'],
                         "description": category['fields']['description']}
                    )
                )

        for category_item in category_list:
            category_for_create.append(
                Category.objects.create(**category_item)
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            if product["model"] == "main.product":
                product_for_create.append(
                    Product(
                        {"id": product['pk'], "name": product['fields']['name'],
                         "description": product['fields']['description'],
                         "price": product['fields']['price'],
                         "category": Category.objects.get(pk=product['fields']['category']),
                         "images": product['fields']['images'], "created_at": product['fields']['created_at'],
                         "updated_at": product['fields']['updated_at']}))

        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(**product_item)
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
