import pytest
from src.category import Category
from src.product import Smartphone, LawnGrass

def test_add_product_valid():
    # Тестируем возможность добавления валидного продукта
    category = Category("Electronics")
    phone = Smartphone("high", "Model X", "128GB", "black")
    category.add_product(phone)
    assert len(category.products) == 1

def test_add_product_invalid():
    # Тестируем попытку добавить недопустимый продукт
    category = Category("Electronics")
    with pytest.raises(TypeError):
        category.add_product("Not a product")  # Ошибка при добавлении неверного типа

def test_add_multiple_products():
    # Тестируем возможность добавления нескольких различных валидных продуктов
    category = Category("Electronics")
    phone = Smartphone("medium", "Model Y", "64GB", "white")
    grass = LawnGrass("USA", "14 days", "green")
    category.add_product(phone)
    category.add_product(grass)
    assert len(category.products) == 2  # Убедимся, что оба продукта добавлены