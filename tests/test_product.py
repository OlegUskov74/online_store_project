import pytest
from src.product import Product


def test_product_init(product):
    """
    [Тест] Проверка инициализации атрибутов.
    """
    assert product.name == "55 QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_price(product):
    """
    [Тест] Тест геттера цены товара.
    """
    assert product.price == 123000.0


def test_price_setter(capsys, product, monkeypatch):
    """
    [Тест] Тест сеттера цены товара.
    """
    product.price = 123000.0
    assert product.price == 123000.0
    product.price = -1000
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 124000.0
    assert product.price == 124000.0
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 120000.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не поменялась"

def test_new_product():
    """
    [Тест] Добавление нового товара.
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 5)
    product.name = "Samsung Galaxy S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 190000.0
    product.quantity = 5

def test_new_product_similar_in_name(product_list, new_product):
    """
    [Тесе] Проверку наличия такого же товара схожего по имени
    """
    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 170000.0,
        "quantity": 7}, product_list)
    assert  new_product.name == "Samsung Galaxy S23 Ultra"
    assert  new_product.description == "256GB, Серый цвет, 200MP камера"
    assert  new_product.price == 190000.0
    assert  new_product.quantity == 12

def test_product_negative(product_fixture_negative):
    """
    [Тест] Негативный исход добавления товара
    """
    product_data, expected_error = product_fixture_negative
    with pytest.raises(ValueError, match=expected_error):
        Product(**product_data)

def test_product_add(product_sum1, product_sum2):
    assert product_sum1 + product_sum2 == 2580000.0

def test_product_add_negative(product_sum1):
    with pytest.raises(TypeError):
        product_sum1 + 1
