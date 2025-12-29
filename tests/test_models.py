import pytest
from unittest.mock import patch
from src.models import Product, Category  # Убедитесь, что импортируете классы из нужного модуля

@pytest.fixture
def setup_category():
    """Создает категорию для тестов."""
    return Category("Фрукты", "Свежие фрукты")

def test_add_product(setup_category):
    product1 = Product("Яблоко", "Сочные яблоки", 50.00, 10)
    setup_category.add_product(product1)

    # Проверяем, что продукт добавлен
    assert len(setup_category._Category__products) == 1

    product2 = Product("Персик", "Сочные персики", 35.00, 5)
    setup_category.add_product(product2)

    # Проверяем, что оба продукта добавлены
    assert len(setup_category._Category__products) == 2

def test_products_property(setup_category):
    product1 = Product("Груша", "Сочные груши", 30.00, 15)
    setup_category.add_product(product1)

    expected_output = "Груша, 30.00 руб. Остаток: 15 шт.\n"
    assert setup_category.products == expected_output

    product2 = Product("Слива", "Сливовые", 20.00, 12)
    setup_category.add_product(product2)

    # Проверяем, что список продуктов формируется корректно
    expected_output = (
        "Груша, 30.00 руб. Остаток: 15 шт.\n"
        "Слива, 20.00 руб. Остаток: 12 шт.\n"
    )
    assert setup_category.products == expected_output

def test_product_price_with_mock(setup_category):
    product = Product("Груша", "Свежие груши", 30.00, 15)
    setup_category.add_product(product)

    assert product.price == 30.00  # Проверяем начальную цену

    with patch('builtins.input', return_value='y'):  # Мокаем ввод, чтобы возвратить 'y'
        product.price = 35.00  # Устанавливаем новую цену
    assert product.price == 35.00  # Проверяем, что цена изменилась

    with patch('builtins.input', return_value='n'):  # Мокаем ввод, чтобы возвратить 'n'
        product.price = 40.00  # Пытаемся установить еще одну цену
    assert product.price == 35.00  # Проверяем, что цена осталась прежней

def test_product_price_negative_value(setup_category):
    product = Product("Яблоко", "Сочные яблоки", 50.00, 10)
    setup_category.add_product(product)

    assert product.price == 50.00  # Проверяем начальную цену
    product.price = -10.00  # Проверяем поведение сеттера при ошибочном значении
    assert product.price == 50.00  # Убедитесь, что цена не изменилась

def test_product_new_product_method():
    product_info = {
        'name': 'Банан',
        'description': 'Сочные бананы',
        'price': 20.00,
        'quantity': 30
    }

    product = Product.new_product(product_info)  # Создаем объект из словаря
    assert product.name == 'Банан'
    assert product.price == 20.00
    assert product.quantity == 30