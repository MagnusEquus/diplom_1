from praktikum.bun import Bun
import data


class TestBuns:

    def test_bun_create_name(self):
        name = data.bun_name
        price = data.bun_price
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_bun_create_price(self):
        name = data.bun_name
        price = data.bun_price
        bun = Bun(name, price)
        assert bun.get_price() == price