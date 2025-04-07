from src.product import Product


class Category:
    """
    Класс для описания категорий

    Атрибуты:
    name (str) : название товара(категория)
    description (str) : описание товара
    products (list) : список товаров категории
    category_count = 0  : количество категорий
    product_count = 0  : количество товаров
    """
    name: str
    description: str
    __products: list[Product] = []

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.description}, {product.price} руб. Остаток: {product.quantity}\n"
        return products_str

    def add_product(self, product: Product):
        """
        Метод в который передаётся объект класса Product
        и уже он записываться в приватный атрибут списка товаров.
        """
        self.__products.append(product)
        Category.product_count += 1

# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#     print(category1.product_count)
#     print(category1.products)
#     print("----------------")
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(category1.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 190000.0,
#          "quantity": 7})
#     print("------------------")
#     category1.add_product(new_product)
#     print(category1.products)
#
#     print("------------------")
#
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)
#
#     print(Category.category_count)
#     print(Category.product_count)
#     print("------------------")
#     print(category1.product_count)
#     print(category1.products)
