import pytest
from src.product import Smartphone, LawnGrass

def test_smartphone_creation():
    phone = Smartphone("high", "Model X", "128GB", "black")
    assert phone.model == "Model X"
    assert phone.efficiency == "high"

def test_lawn_grass_creation():
    grass = LawnGrass("USA", "14 days", "green")
    assert grass.country == "USA"
    assert grass.germination_period == "14 days"

def test_product_addition():
    phone = Smartphone("high", "Model X", "128GB", "black")
    grass = LawnGrass("USA", "14 days", "green")
    # Проверка выброса ошибки при сложении разных классов
    with pytest.raises(TypeError):
        phone + grass

def test_add_product_method():
    grass = LawnGrass("USA", "14 days", "green")
    phone = Smartphone("high", "Model X", "128GB", "black")
    with pytest.raises(TypeError):
        grass.add_product("Not a product")  # Проверка выброса ошибки