from praktikum.database import Database
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('bun_name,bun_price',
                             [
                                 ['black bun', 100],
                                 ['white bun', 200],
                                 ['red bun', 300]
                             ]
                             )
    def test_buns(self, bun_name, bun_price):
        database = Database()
        names = []
        prices = []
        for bun in database.available_buns():
            names.append(bun.get_name())
            prices.append(bun.get_price())
        assert bun_name in names and bun_price in prices

    @pytest.mark.parametrize('ingredient_name,ingredient_price,ingredient_type',
                             [
                                 ['hot sauce', 100, INGREDIENT_TYPE_SAUCE],
                                 ['sour cream', 200, INGREDIENT_TYPE_SAUCE],
                                 ['chili sauce', 300, INGREDIENT_TYPE_SAUCE],
                                 ['cutlet', 100, INGREDIENT_TYPE_FILLING],
                                 ['dinosaur', 200, INGREDIENT_TYPE_FILLING],
                                 ['sausage', 300, INGREDIENT_TYPE_FILLING]
                             ]
                             )
    def test_ingredients(self, ingredient_name, ingredient_price, ingredient_type):
        database = Database()
        names = []
        prices = []
        types = []
        for ingredient in database.available_ingredients():
            names.append(ingredient.get_name())
            prices.append(ingredient.get_price())
            types.append(ingredient.get_type())
        assert ingredient_name in names and ingredient_price in prices and ingredient_type in types