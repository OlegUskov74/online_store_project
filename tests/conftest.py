import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def firs_product():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ]
    )


@pytest.fixture
def second_product():
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
