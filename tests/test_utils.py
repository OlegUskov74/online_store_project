import json
from unittest.mock import patch, mock_open

import pytest
import os

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

