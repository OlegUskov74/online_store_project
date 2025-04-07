import pytest
from src.category import Category
from src.product import Product



def test_category_init(firs_product, second_product):
    assert firs_product.name == "Смартфоны"
    assert firs_product.description == "Смартфоны, как средство не только коммуникации"

    assert second_product.name == "Телевизоры"
    assert second_product.description == "Современный телевизор"

    assert firs_product.category_count == 2
    assert second_product.category_count == 2

    assert firs_product.product_count == 5
    assert second_product.product_count == 5


def test_products_init(firs_product):
    assert firs_product.products == (
        "Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0 руб. Остаток: 5\n"
        "Iphone 15, 512GB, Gray space, 210000.0 руб. Остаток: 8\n")

# def test_add_product(firs_product, product):
#     # assert firs_product.product_count == 2
#     firs_product.add_product = product
#     assert firs_product.product_count == 3

