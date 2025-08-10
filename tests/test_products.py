import time

import pytest

from utils.commonUtils import CommonUtils


@pytest.mark.usefixtures("setup")
class Test_Products:

    @pytest.mark.product
    @pytest.mark.parametrize("username, password, product_name", [
        ("standard_user", "secret_sauce", "Sauce Labs Backpack")])
    def test_add_to_cart_product(self, username, password, product_name):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        self.product.open_product_details_screen(product_name)
        self.product.add_to_cart_product()

    @pytest.mark.product
    @pytest.mark.parametrize("username, password, product_name, value", [
        ("standard_user", "secret_sauce", "Sauce Labs Bike Light","1")])
    def test_verify_adding_a_single_product_to_cart(self,username, password, product_name, value):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        self.product.open_product_details_screen(product_name)
        self.product.add_to_cart_product()
        assert self.product.check_cart_value(value)

    @pytest.mark.product
    @pytest.mark.parametrize("username, password, product_name, value", [
        ("standard_user", "secret_sauce", "Sauce Labs Bike Light", "1")])
    def test_verify_user_can_navigate_to_cart_screen(self, username, password, product_name, value):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        self.product.open_product_details_screen(product_name)
        self.product.add_to_cart_product()
        assert self.product.check_cart_value(value)
        self.product.navigate_to_cart_screen()
        assert self.cart.verify_cart_screen()

