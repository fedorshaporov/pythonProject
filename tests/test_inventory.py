import pytest
from src.inventory import Product, Category

def test_product_str():
    product = Product(name="Товар 1", description="Описание товара 1", price=80.0, quantity=15)
    assert str(product) == "Товар 1, 80.00 руб. Остаток: 15 шт."

def test_category_str():
    category = Category(name="Продукты", description="Описание категории")
    category.add_product(Product(name="Товар 1", description="Описание товара 1", price=80.0, quantity=15))
    category.add_product(Product(name="Товар 2", description="Описание товара 2", price=100.0, quantity=5))
    assert str(category) == "Продукты, количество продуктов: 20 шт."

def test_product_addition():
    product_a = Product(name="Товар A", description="Описание товара A", price=100, quantity=10)
    product_b = Product(name="Товар B", description="Описание товара B", price=200, quantity=2)
    assert product_a + product_b == 1400  # (100 * 10) + (200 * 2)

def test_product_addition_invalid():
    product_a = Product(name="Товар A", description="Описание товара A", price=100, quantity=10)
    with pytest.raises(TypeError):
        result = product_a + "Неправильный тип"  # Должно выбросить ошибку
