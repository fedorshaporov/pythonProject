import pytest
from src.main import Product, Category, Smartphone, LawnGrass

def test_product_creation():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.description == "Описание товара"
    assert product.price == 100.0
    assert product.quantity == 10

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
    grass = LawnGrass("Груша газонная", "Газонная трава", 1500, 30, "Россия", 14, "зеленый")
    assert grass.name == "Груша газонная"
    assert grass.description == "Газонная трава"
    assert grass.price == 1500
    assert grass.quantity == 30
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "зеленый"

def test_category_add_product():
    category = Category("Электроника", "Электронные устройства")
    product = Product("Товар", "Описание товара", 100.0, 10)
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0] == product

def test_category_add_invalid_product():
    category = Category("Электроника", "Электронные устройства")
    with pytest.raises(TypeError):
        category.add_product("Некорректный объект")

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

def test_product_setter_price_negative():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = -50  # Установим отрицательную цену
    assert product.price == 100.0  # Убедитесь, что цена не изменилась

def test_product_setter_price_zero():
    product = Product("Товар", "Описание товара", 100.0, 10)
    product.price = 0  # Установим нулевую цену
    assert product.price == 100.0  # Убедитесь, что цена не изменилась

def test_product_addition_within_same_class():
    smartphone1 = Smartphone("Смартфон 1", "Описание 1", 20000, 5, 5, "Model X1", 128, "синий")
    smartphone2 = Smartphone("Смартфон 2", "Описание 2", 25000, 2, 8, "Model X2", 256, "черный")
    assert smartphone1 + smartphone2 == (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)

def test_lawn_grass_attributes():
    grass = LawnGrass("Груша газонная", "Газонная трава", 1500, 30, "Россия", 14, "зеленый")
    assert grass.country == "Россия"
    assert grass.germination_period == 14
