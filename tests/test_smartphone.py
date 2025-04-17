import pytest


def test_smartphone_init(smartphone_product1):
    """
    [Тест] Инициализация класс-наследник для продукта «Смартфон». Родительский класс Product
    """
    assert smartphone_product1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product1.price == 180000.0
    assert smartphone_product1.quantity == 5
    assert smartphone_product1.efficiency == 95.5
    assert smartphone_product1.model == "S23 Ultra"
    assert smartphone_product1.memory == 256
    assert smartphone_product1.color == "Серый"

def test_smartphone_add(smartphone_product1, smartphone_product2):
    """
    [Тест] Сложение двух продуктов одного класса
    """
    assert smartphone_product1 + smartphone_product2 == 2580000.0

def test_smartphone_add_error(smartphone_product1, lawn_grass_product1):
    """
    [Тест] Возбуждение ошибки при сложении двух продуктов разных классов
    """
    with pytest.raises(TypeError):
        result = smartphone_product1 + lawn_grass_product1