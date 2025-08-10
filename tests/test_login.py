import time
import pytest
from screens.login import Login
from screens.products import Products
from utils.commonUtils import CommonUtils


@pytest.mark.usefixtures("setup")
class Test_Login:

    @pytest.mark.login
    @pytest.mark.parametrize("username, password", [
        ("standard_user", "secret_sauce")])
    def test_verify_valid_login(self, username, password):
        self.login.enter_username(username)
        self.login.enter_password(password)
        self.login.tap_login()
        assert self.product.verify_product_screen()
        CommonUtils.get_logger().info("login successful")

    @pytest.mark.login
    @pytest.mark.parametrize("credentials", [CommonUtils.generate_fake_candidate_data()])
    def test_verify_invalid_login(self,credentials):
        self.login.enter_username(credentials['username'])
        self.login.enter_password(credentials['password'])
        self.login.tap_login()
        assert self.login.get_error_text() == "Username and password do not match any user in this service."
