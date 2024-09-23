import pytest
from praktikum.bun import Bun
import data
from praktikum.ingredient import Ingredient
from unittest.mock import Mock

@pytest.fixture()
def create_bun_mock():
    bun = Mock()
    bun.get_name.return_value = data.bun_name
    bun.get_price.return_value = data.bun_price
    yield bun


@pytest.fixture()
def create_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = data.ingredient_type
    ingredient.get_name.return_value = data.ingredient_name
    ingredient.get_price.return_value = data.ingredient_price
    yield ingredient
