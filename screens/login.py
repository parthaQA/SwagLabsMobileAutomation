from appium.webdriver.common.appiumby import AppiumBy
from utils.commonUtils import CommonUtils


class Login(CommonUtils):


    username_field = (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    password_field = (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    login_button = (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
    error_msg = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Error message']//android.widget.TextView")

    def __init__(self, driver):
        super().__init__(driver)


    def enter_username(self, username):
        self.enter_text(self.username_field, username)


    def enter_password(self, password):
        self.enter_text(self.password_field, password)


    def tap_login(self):
        self.tap_button(self.login_button)

    def get_error_text(self):
        return self.validate_text(self.error_msg)



