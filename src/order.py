from typing import Union

from src.category import Category
from src.product import Product



class Order(Category):
    """
    Класс-наследник для категории «Заказ». Родительский класс Category.
     В котором будет ссылка на то, какой товар был куплен,
     количество купленного товара, а также итоговая стоимость.
     В заказе может быть указан только один товар.

    Атрибуты:
    quantity purchased(int) : количество купленного товара
    total cost (Union[int, float]) : итоговая стоимость
    """
    quantity_purchased: int = 0
    total_cost: Union[int, float] = 0

    def __init__(self, name, description, products, quantity_purchased, total_cost):
        super().__init__(name, description, products)
        self.quantity_purchased = quantity_purchased
        self.total_cost = total_cost


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 1)
#
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     category1 = Order("Смартфоны","Заказ",[product1], 190000.0, 1)
#
#     print(category1.quantity_purchased)
#     print(category1.total_cost)