from inventory import Product, Category

def main():
    # Примеры использования
    product1 = Product("Товар 1", "Описание товара 1", 80.0, 15)
    product2 = Product("Товар 2", "Описание товара 2", 120.0, 10)

    category = Category("Продукты", "Описание категории")
    category.add_product(product1)
    category.add_product(product2)

    print(category)  # вывод категории
    print(product1)  # вывод продукта

if __name__ == "__main__":
    main()
