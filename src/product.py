
class Product:
    def __init__(self, category):
        self.category = category

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        # Объедините товары здесь (если необходимо)


class Smartphone(Product):
    def __init__(self, efficiency, model, memory, color):
        super().__init__("Смартфоны")
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, country, germination_period, color):
        super().__init__("Трава газонная")
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def add_product(self, product):
        if not isinstance(product, (Smartphone, LawnGrass)):
            raise TypeError(
                "Можно добавлять только продукты или их наследники"
            )
        # Логика добавления продукта в категорию
