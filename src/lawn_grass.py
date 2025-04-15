from src.product import Product


class LawnGrass(Product):
    """
    Класс для продукта «Трава газонная». Родительский класс Product

    Атрибуты:
    country : страна-производитель
    germination_period : срок прорастания
    color : цвет
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
