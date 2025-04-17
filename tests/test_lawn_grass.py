import pytest



def test_lawn_grass_init(lawn_grass_product1):
    """
    [Тест] Инициализация класс-наследник для продукта «Трава газонная». Родительский класс Product
    """
    assert lawn_grass_product1.name == "Газонная трава"
    assert lawn_grass_product1.description == "Элитная трава для газона"
    assert lawn_grass_product1.price == 500.0
    assert lawn_grass_product1.quantity == 20
    assert lawn_grass_product1.country == "Россия"
    assert lawn_grass_product1.germination_period == "7 дней"
    assert lawn_grass_product1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass_product1, lawn_grass_product2):
    """
    [Тест] Сложение двух продуктов одного класса
    """
    assert lawn_grass_product1 + lawn_grass_product2 == 16750.0


def test_lawn_grass_add_error(lawn_grass_product1, smartphone_product1):
    """
    [Тест] Возбуждение ошибки при сложении двух продуктов разных классов
    """
    with pytest.raises(TypeError):
        result = lawn_grass_product1 + smartphone_product1

