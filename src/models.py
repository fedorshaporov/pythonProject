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

    @classmethod
    def new_product(cls, product_info: dict) -> 'Product':
        """Создает новый экземпляр продукта на основе информации из словаря."""
        return cls(
            product_info['name'],
            product_info['description'],
            product_info['price'],
            product_info['quantity']
        )

class Category:
    category_count = 0  # Счетчик категорий
    product_count = 0   # Счетчик продуктов

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут для хранения продуктов
        Category.category_count += 1

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1
        print(f"Продукт {product.name} добавлен в категорию {self.name}.")

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами в категории."""
        return "".join(
            f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products
        )
