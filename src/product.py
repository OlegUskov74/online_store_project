
from typing import Union, Dict, Hashable, Any
from src.base_product import BaseProduct
from src.print_mixin import PrintMixin



class Product(BaseProduct, PrintMixin):
    """
    Класс для описания продукта по категориям

    Атрибуты:
    name (str) : название товара в категории "products"
    description (str) : описание товара
    price (Union[int, float]) : цена товара
    quantity (int) : количество в наличии
    """
    name: str
    description: str
    __price: Union[int, float]
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

        if self.__price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if self.quantity < 0:
            raise ValueError("Количество не может быть отрицательным")


    def __str__(self):
        """
        Магический метод отображения информации об объекте класса Product для пользователей
        :return: строка в виде 'Название продукта, ?? руб. Остаток: ?? шт.'
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        """
        Магический метод, для сложения цены и количества в наличии
        :return:Общая цена продукта на складе
        """
        if type(other) is Product:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @property
    def price(self):
        """
        Гетер, который возвращает цену товара.
        :return: Приватный атрибут цены.
        """
        return self.__price

    @price.setter
    def price(self, nev_prise):
        """
        Сеттер, реализуйте проверку,
        а так же в случае если цена товара понижается, добавить логику подтверждения пользователем вручную
        :param nev_prise: Новая цена за товар
        """
        if nev_prise <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif nev_prise < self.__price:
            confirmation = (
                input(f"Вы хотите изменить цену {self.__price} на цену {nev_prise} (y/n)").strip().lower())
            if confirmation == "y":
                self.__price = nev_prise
                print(f"Цена изменена на {nev_prise}")
            else:
                print("Цена не поменялась")
        else:
            self.__price = nev_prise

    @classmethod
    def new_product(cls, product_parameters: Dict[Hashable, Any], similar_product: list = None):
        """
        Класс-Метод, который будет принимать на вход параметры товара в словаре и возвращать созданный объект класса Product.
        А также проверку наличия такого же товара схожего по имени. В случае если товар уже существует, складывает количество в наличии старого товара и нового.
        При конфликте цен выбрать ту, которая является более высокой.
        :param product_parameters: Параметры товара в виде словаря.
        :param similar_product: Список товаров, в котором нужно искать дубликаты (тип лист словарей)
        :return: Созданный объект класса Product.
        """
        product = cls(
            name=product_parameters["name"],
            description=product_parameters["description"],
            quantity=product_parameters["quantity"],
            price=product_parameters["price"], )

        if similar_product:
            for item in similar_product:
                if product.name == item["name"]:
                    product.quantity += item["quantity"]
                    if product.price < item["price"]:
                        product.price = item["price"]

        return product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 35000.0, 14)
    # product4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 10)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    product_list = [{
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 190000.0,
        "quantity": 5,},
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 35000.0, "quantity": 14}]


    new_product =Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 170000.0,
        "quantity": 7},
        product_list)

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print("-------------------")

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

