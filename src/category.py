from src.product import Smartphone, LawnGrass
# Импортируем только классы, которые используем


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if not isinstance(product, (Smartphone, LawnGrass)):
            raise TypeError(
                "Можно добавлять только продукты или их наследники"
            )
        self.products.append(product)
