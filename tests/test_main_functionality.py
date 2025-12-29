import pytest
from src.product import Smartphone, LawnGrass
from src.category import Category

def test_main_functionality():
    # Создаём категорию смартфонов
    smartphones = Category("Smartphones")

    # Создаем экземпляр смартфона
    phone = Smartphone("high", "Model X", "128GB", "black")

    # Добавляем смартфон в категорию и проверяем
    smartphones.add_product(phone)
    assert len(smartphones.products) == 1

    # Проверяем, что добавление неверного типа вызывает ошибку
    with pytest.raises(TypeError):
        smartphones.add_product("Not a product")  # Должен выбросить TypeError

def test_lawn_grass_functionality():
    # Создаем категорию травы
    lawn_grass = Category("Lawn Grass")

    # Создаем экземпляр травы газонной
    grass = LawnGrass("USA", "14 days", "green")

    # Добавляем траву в категорию и проверяем
    lawn_grass.add_product(grass)
    assert len(lawn_grass.products) == 1

    # Проверяем, что добавление неверного типа вызывает ошибку
    with pytest.raises(TypeError):
        lawn_grass.add_product("Not a product")  # Должен выбросить TypeError