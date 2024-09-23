from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

bun_name = 'Bun_test'
bun_price = 123

ingredient_name = 'test_filling'
ingredient_price = 123
ingredient_type = INGREDIENT_TYPE_FILLING

ingredient2_name = 'test_sauce'
ingredient2_price = 321
ingredient2_type = INGREDIENT_TYPE_SAUCE

database_bun = Bun("black bun", 100)
database_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)