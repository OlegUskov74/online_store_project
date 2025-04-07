import json
from unittest.mock import patch, mock_open

import pytest
import os

from config import PATH_JSON
from src.utils import read_json, creade_objects_from_json


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_read_json(mock_file):
    expected_result = [{"id": 1, "amount": 100}]
    assert read_json("../data/products.json") == expected_result

@patch("builtins.open", new_callable=mock_open, read_data="[{'id': 1, 'amount': 100}]")
def test_get_transactions_data_invalid_json(mock_json_load):
    assert read_json("dummy_path.json") == []
    mock_json_load.assert_called_once()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_transactions_data_file_not_found(mock_file):
    assert read_json("missing_file.json") == []

@patch("builtins.open", side_effect=json.JSONDecodeError)
def test_get_transactions_data_error(mock_file):
    assert read_json("dummy_path.json") == []

def test_creade_objects_from_json() -> None:
    """
    [Тест] Создание объектов класса.
    """
    assert creade_objects_from_json(read_json(PATH_JSON))[0].name == "Смартфоны"
    assert creade_objects_from_json(read_json(PATH_JSON))[0].description == ("Смартфоны, как средство не только коммуникации, "
                                                                             "но и получение дополнительных функций для удобства жизни")
    assert creade_objects_from_json(read_json(PATH_JSON))[0].products == ("Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0 руб. Остаток: 5\n" 
                                                                          "Iphone 15, 512GB, Gray space, 210000.0 руб. Остаток: 8\n"
                                                                          "Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0 руб. Остаток: 14\n")
