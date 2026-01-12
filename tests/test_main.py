import pytest
from src.main import Product, Smartphone, LawnGrass, Category


# Тест для проверки бросаемого исключения при создании товара с нулевым количеством
def test_product_creation_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Товар", "Описание товара", 100.0, 0)  # Создание с нулевым количеством

# Тест для проверки среднего ценника в категории
def test_category_average_price_no_products():
    category = Category("Тестовая категория", "Тестовое описание")
    assert category.average_price() == 0  # Проверяем, что возвращается 0

def test_category_average_price_with_products():
    category = Category("Тестовая категория", "Тестовое описание")
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    expected_average = (100.0 + 200.0) / 2
    assert category.average_price() == expected_average  # Проверяем среднюю цену

def test_product_creation():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_update():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = 150.0  # Обновляем цену
    assert product.price == 150.0  # Проверяем, что цена обновилась

def test_product_quantity_update():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.quantity = 20  # Обновляем количество
    assert product.quantity == 20  # Проверяем, что количество обновилось

def test_product_quantity_update_invalid():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.quantity = -5  # Устанавливаем отрицательное количество
    assert product.quantity == 10  # Проверяем, что количество не изменилось

def test_category_total_products():
    category = Category("Тестовая категория", "Тестовое описание")
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    total_quantity = sum(product.quantity for product in category._products)
    assert total_quantity == 8  # Проверяем общее количество продуктов в категории

def test_category_str_method():
    category = Category("Устройства", "Разные устройства")
    product1 = Product("Смартфон", "Описание смартфона", 10000, 5)
    product2 = Product("Планшет", "Описание планшета", 15000, 3)
    category.add_product(product1)
    category.add_product(product2)

    expected_str = "Устройства, количество продуктов: 8 шт."
    assert str(category) == expected_str  # Проверяем строковое представление категории

def test_smartphone_color():
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    assert smartphone.color == "Серый"  # Проверяем цвет устройства

def test_lawn_grass_country():
    grass = LawnGrass("Газонная трава", "Описание", 1500, 30, "Россия", 14, "зеленый")
    assert grass.country == "Россия"  # Проверяем страну происхождения

# Тесты предыдущие
def test_product_setter_price_negative():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = -50  # Устанавливаем отрицательную цену
    assert product.price == 100.0  # Убедитесь, что цена не изменилась

def test_product_setter_price_zero():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = 0  # Устанавливаем нулевую цену
    assert product.price == 100.0  # Убедитесь, что цена не изменилась

def test_smartphone_creation():
    smartphone = Smartphone("Смартфон", "Современный смартфон", 25000, 15, 8, "Model X", 256, "черный")
    assert smartphone.name == "Смартфон"
    assert smartphone.description == "Современный смартфон"
    assert smartphone.price == 25000
    assert smartphone.quantity == 15
    assert smartphone.efficiency == 8
    assert smartphone.model == "Model X"
    assert smartphone.memory == 256
    assert smartphone.color == "черный"

def test_lawn_grass_creation():
    grass = LawnGrass("Газонная трава", "Описание", 1500, 30, "Россия", 14, "зеленый")
    assert grass.name == "Газонная трава"
    assert grass.description == "Описание"
    assert grass.price == 1500
    assert grass.quantity == 30
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "зеленый"

def test_category_add_product():
    category = Category("Электроника", "Описание")
    product = Product("Товар", "Описание товара", 100.0, 10)
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0] == product

def test_category_add_invalid_product():
    category = Category("Электроника", "Описание")
    with pytest.raises(TypeError):
        category.add_product("Некорректный объект")  # Проверка на ошибку при добавлении

def test_product_addition_and_sum():
    smartphone1 = Smartphone("Смартфон 1", "Описание 1", 20000, 5, 5, "Model X1", 128, "синий")
    smartphone2 = Smartphone("Смартфон 2", "Описание 2", 25000, 2, 8, "Model X2", 256, "черный")

    total_value = smartphone1 + smartphone2
    expected_value = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
    assert total_value == expected_value

def test_product_addition_type_error():
    smartphone = Smartphone("Смартфон", "Описание", 20000, 5, 5, "Model X", 128, "синий")
    grass = LawnGrass("Газонная трава", "Описание", 1500, 30, "Россия", 14, "зеленый")

    with pytest.raises(TypeError):
        smartphone + grass  # Ожидаем ошибку при сложении разных типов

def test_main_logic():
    """Тестирует работу логики в блоке if __name__ == '__main__'."""
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")

    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    category_smartphones.add_product(smartphone1)
    category_smartphones.add_product(smartphone2)
    category_smartphones.add_product(smartphone3)

    assert len(category_smartphones._products) == 3  # Проверка добавленных продуктов

    expected_output = (
        f"{smartphone1.name}, {smartphone1.price} руб. Остаток: {smartphone1.quantity} шт.\n" +
        f"{smartphone2.name}, {smartphone2.price} руб. Остаток: {smartphone2.quantity} шт.\n" +
        f"{smartphone3.name}, {smartphone3.price} руб. Остаток: {smartphone3.quantity} шт."
    )

    assert category_smartphones.products.strip() == expected_output.strip()