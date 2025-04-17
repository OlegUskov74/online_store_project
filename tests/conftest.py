import pytest

from src.category import Category
from src.product import Product
from src.my_iterator import MyIterator
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def product():
    return Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)

@pytest.fixture
def product_list():
    return [
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 190000.0,
            "quantity": 5
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 35000.0,
            "quantity": 14
        }
    ]

@pytest.fixture
def new_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 170000.0,
        "quantity": 7
    }

@pytest.fixture(
    params=[({"name": "Xiaomi Redmi", "description": "Красный", "price": -100, "quantity": 14},
            "Цена не может быть отрицательной"),
            ({"name": "Xiaomi Redmi", "description": "Красный", "price": 31000, "quantity": -14},
            "Количество не может быть отрицательным")])
def product_fixture_negative(request):
    return request.param

@pytest.fixture
def product_sum1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def product_sum2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

@pytest.fixture
def product_iterator(second_product):
    return MyIterator(second_product)

@pytest.fixture
def smartphone_product1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                            "S23 Ultra", 256, "Серый")

@pytest.fixture
def smartphone_product2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def lawn_grass_product1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def lawn_grass_product2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
