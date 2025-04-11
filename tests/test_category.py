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
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n")

def test_category_str(firs_product):
    assert  str(firs_product) == "Смартфоны, количество продуктов: 13 шт."

def test_my_iterator(product_iterator):
    """
    [Тест] Тест итератора класса MyIterator
    """
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(product_iterator)
