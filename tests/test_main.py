import unittest

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1


    def add_product(self, product: Product):
        self.products.append(product)
        Category.product_count += 1


class TestProductCategory(unittest.TestCase):


    def setUp(self):
        # Сбросить подсчеты перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0


    def test_product_initialization(self):
        product = Product("Laptop", "A powerful laptop", 999.99, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "A powerful laptop")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.quantity, 10)


    def test_category_initialization(self):
        category = Category("Electronics", "Devices and gadgets")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Devices and gadgets")
        self.assertEqual(len(category.products), 0)
        self.assertEqual(Category.category_count, 1)  # Должно быть 1


    def test_add_product_to_category(self):
        category = Category("Electronics", "Devices and gadgets")
        product = Product("Smartphone", "Latest model smartphone", 499.99, 5)
        category.add_product(product)

        self.assertEqual(len(category.products), 1)
        self.assertEqual(category.products[0].name, "Smartphone")
        self.assertEqual(Category.product_count, 1)  # Должно быть 1

        # Добавление еще одного продукта
        product2 = Product("Headphones", "Wireless headphones", 199.99, 15)
        category.add_product(product2)

        self.assertEqual(len(category.products), 2)  # Должно быть 2
        self.assertEqual(Category.product_count, 2)  # Должно быть 2

if __name__ == '__main__':
    unittest.main()
