from praktikum.burger import Burger
import data
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_bun(self, create_bun_mock):
        bun = create_bun_mock
        burger = Burger()
        burger.set_buns(bun)
        assert bun.get_name() in burger.get_receipt()

    def test_add_ingredient(self, create_bun_mock, create_ingredient_mock):
        ingredient = create_ingredient_mock
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.set_buns(create_bun_mock)
        assert create_ingredient_mock.get_type().lower() in burger.get_receipt()

    def test_remove_ingredient(self, create_bun_mock, create_ingredient_mock):
        ingredient = create_ingredient_mock
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.set_buns(create_bun_mock)
        burger.remove_ingredient(0)
        assert create_ingredient_mock.get_type().lower() not in burger.get_receipt()

    def test_move_ingredient(self, create_bun_mock, create_ingredient_mock):
        ingredient = create_ingredient_mock
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.set_buns(create_bun_mock)
        ingredient2 = Ingredient(data.ingredient2_type, data.ingredient2_name, data.ingredient2_price)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.get_receipt().find(ingredient.get_name()) > burger.get_receipt().find(ingredient2.get_name())

    def test_price(self, create_bun_mock, create_ingredient_mock):
        ingredient = create_ingredient_mock
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.set_buns(create_bun_mock)
        sum = create_ingredient_mock.get_price() + create_bun_mock.get_price() * 2
        assert sum == burger.get_price()
