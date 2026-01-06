class Product:
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
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
        # Проверка, является ли другой объект тем же типом (или наследником)
        if not isinstance(other, self.__class__):
            raise TypeError("Можно складывать только товары одного типа.")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float,
                 quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self._products = []  # Приватный атрибут

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты классов Product "
                "или его наследников."
            )
        self._products.append(product)

    @property
    def products(self):
        return ''.join(str(product) for product in self._products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


# Пример использования - тестирование создания объектов
if __name__ == "__main__":
    electronics = Category("Электроника", "Электронные устройства")
    lawn_care = Category("Уход за газоном", "Товары для ухода за газоном")

    smartphone = Smartphone(
        "Смартфон", "Современный смартфон", 25000, 15, 8,
        "Model X", 256, "черный"
    )
    grass = LawnGrass(
        "Груша газонная", "Газонная трава", 1500, 30,
        "Россия", 14, "зеленый"
    )

    electronics.add_product(smartphone)
    lawn_care.add_product(grass)

    print(electronics.products)
    print(lawn_care.products)

    # Проверка сложения
    print(smartphone + smartphone)  # Сложение двух смартфонов
