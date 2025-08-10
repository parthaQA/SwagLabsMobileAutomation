import pytest

from utils.commonUtils import CommonUtils


@pytest.mark.usefixtures("setup")
class TestCart:

    @pytest.mark.cart
    @pytest.mark.parametrize("username, password, product_name, value", [
        ("standard_user", "secret_sauce", "Sauce Labs Bike Light", "1")])
    def test_number_of_prouducts_in_cart(self, username, password, product_name, value):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        self.product.open_product_details_screen(product_name)
        self.product.add_to_cart_product()
        assert self.product.check_cart_value(value)
        self.product.navigate_to_cart_screen()
        assert self.cart.verify_cart_screen()
        print(self.cart.number_of_products_in_cart())
        CommonUtils.get_logger().info(f"cart value is {self.cart.number_of_products_in_cart()}")

    @pytest.mark.cart
    @pytest.mark.parametrize("username, password, product_name, value", [
        ("standard_user", "secret_sauce", "Sauce Labs Bike Light", "1")])
    def test_remove_products_from_cart(self, username, password, product_name, value):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        self.product.open_product_details_screen(product_name)
        self.product.add_to_cart_product()
        assert self.product.check_cart_value(value)
        self.product.navigate_to_cart_screen()
        assert self.cart.verify_cart_screen()
        print(self.cart.number_of_products_in_cart())
        CommonUtils.get_logger().info(f"cart value is {self.cart.number_of_products_in_cart()}")
        print("element", self.cart.remove_product())
        assert self.cart.remove_product() is True
