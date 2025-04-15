from src.product import Product



class Smartphone(Product):
    """
    Класс для продукта «Смартфон». Родительский класс Product

    Атрибуты:
    efficiency : производительность
    model : модель
    memory : объем встроенной памяти
    color : цвет
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color