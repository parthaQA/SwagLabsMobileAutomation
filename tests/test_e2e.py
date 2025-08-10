import pytest
from utils.commonUtils import CommonUtils


@pytest.mark.usefixtures("setup")
class TestE2E:

    @pytest.mark.e2e
    @pytest.mark.parametrize("username, password, product_name, value", [
        ("standard_user", "secret_sauce", "Sauce Labs Bike Light", "1")])
    def test_verify_user_can_purchase_a_single_product(self, username, password, product_name, value):
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
        price = self.cart.get_product_amount()
        print("product price", price)
        self.cart.navigate_to_checkout_screen()
        self.checkout.verify_checkout_screen()
        data = CommonUtils.generate_fake_candidate_data()
        self.checkout.enter_first_name(data["username"])
        self.checkout.enter_last_name(data["lastname"])
        self.checkout.enter_postal_code(data["postalcode"])
        self.checkout.tap_continue_button()
        assert self.checkout.verify_checkout_overview_screen()
        assert self.checkout.product_information(product_name)
        assert self.checkout.product_price(price)
        self.checkout.tap_on_finish_button()
        assert self.checkout.get_successful_purchase()