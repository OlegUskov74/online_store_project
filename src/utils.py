import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """
    Функция открывает файл json
    :param path: файл json
    :return: список словарей
    """
    try:
        full_path = os.path.abspath(path)
        with open(full_path, 'r', encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:        # Ошибка, файл не найден
        return []
    except json.JSONDecodeError:     # Ошибка, содержит неверные данные (ошибка JSON)
        return []
    except (TypeError, ValueError):  # Ошибка обработки данных
        return []


def creade_objects_from_json(data: list[dict]) -> Any:
    """
    Функция создает объекты из json файла
    :param data: файл json
    """
    products = []                              # список для заполнения экземпляров класса Category
    for category in data:                      # переберем категории
        product = []                           # список для заполнения товаров категорий по ключу 'products'
        for task in category['products']:      # переберем список(словарь) товаров по ключу 'products'
            product.append(Product(**task))    # распаковываем словарь товаров и добавляем в экземпляр класс Product
        category['products'] = product         # переписываем значение в список -> list[dict]
        products.append(Category(**category))  # распаковываем словарь товаров и добавляем в экземпляр класс Category
    return products

# if __name__ == "__main__":
#     data = read_json("../data/products.json")
#     result = creade_objects_from_json(data)
#
#     print(result)
#     print(result[0].name)
#     print(result[0].products)
