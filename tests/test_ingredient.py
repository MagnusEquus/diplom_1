import data
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_type(self):
        name = data.ingredient_name
        price = data.ingredient_price
        type = data.ingredient_type
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    def test_name(self):
        name = data.ingredient_name
        price = data.ingredient_price
        type = data.ingredient_type
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    def test_price(self):
        name = data.ingredient_name
        price = data.ingredient_price
        type = data.ingredient_type
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price