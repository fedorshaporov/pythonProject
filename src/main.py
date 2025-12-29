from src.product import Smartphone, LawnGrass
# Убедитесь, что здесь правильные импорты
from src.category import Category

# Создаем категории
smartphones = Category("Смартфоны")
lawn_grasses = Category("Трава газонная")

# Создаем продукты
phone = Smartphone("high", "Model X", "128GB", "black")
grass = LawnGrass("USA", "14 days", "green")

# Добавляем продукты в категории
smartphones.add_product(phone)
lawn_grasses.add_product(grass)

# Проверяем добавление неверного типа
try:
    smartphones.add_product("Not a product")  # Должен выбросить TypeError
except TypeError as e:
    print(f"Ошибка: {e}")

# Проверяем список продуктов в категории
print("Продукты в категории Смартфоны:", smartphones.products)
print("Продукты в категории Трава газонная:", lawn_grasses.products)
