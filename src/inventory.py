class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для хранения цены
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
        else:
            confirmation = input(
                f"Согласны на изменение цены с {self.__price:.2f} "
                f"на {new_price:.2f}? (y/n): "
            )
            if confirmation.lower() == 'y':
                self.__price = new_price
                print(f"Цена изменена на {new_price:.2f}.")
            else:
                print("Изменение цены отменено.")

    def __str__(self):
        return (f"{self.name}, {self.price:.2f} руб. Остаток: "
                f"{self.quantity} шт.")

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity +
                    other.price * other.quantity)
        raise TypeError("Сложение возможно только с другим объектом Product")


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения продуктов
        Category.category_count += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return (f"{self.name}, количество продуктов: "
                f"{total_quantity} шт.")

