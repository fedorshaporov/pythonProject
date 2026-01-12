class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Можно складывать только товары одного типа.")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0  # Класс-атрибут для хранения количества категорий
    product_count = 0   # Класс-атрибут для хранения общего количества продуктов

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.category_count += 1  # Увеличиваем количество категорий при создании новой

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты классов Product или его наследников.")
        self._products.append(product)
        Category.product_count += 1  # Увеличиваем количество продуктов при добавлении

    @property
    def products(self):
        return '\n'.join(str(product) for product in self._products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == "__main__":
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 7, "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", 5, "Темно-зеленый")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")
    category_grass = Category("Газонная трава", "Различные виды газонной травы")

    category_smartphones.add_product(smartphone1)
    category_smartphones.add_product(smartphone2)
    category_smartphones.add_product(smartphone3)

    category_grass.add_product(grass1)
    category_grass.add_product(grass2)

    # Вывод общего количества категорий и продуктов
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество продуктов: {Category.product_count}")

    # Вывод продуктов в категориях
    print(category_smartphones.products)
    print(category_grass.products)

    # Проверка сложения
    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
