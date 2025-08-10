import time

from appium.webdriver.common.appiumby import AppiumBy

from utils.commonUtils import CommonUtils


class Products(CommonUtils):

    product_screen = (AppiumBy.XPATH, "//android.widget.TextView[@text='PRODUCTS']")
    cart_icon = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']")

    def __init__(self, driver):
        super().__init__(driver)


    def verify_product_screen(self):
        return self.is_element_displayed(self.product_screen)

    def open_product_details_screen(self, product_name):
        time.sleep(3)
        product_ = (AppiumBy.XPATH,
                    "//android.widget.TextView[@text='" + product_name + "']")
        print(product_)
        self.tap_button(product_)

    def add_to_cart_product(self):
        add_cart = (AppiumBy.XPATH, "//android.widget.TextView[@text='ADD TO CART']")
        assert self.scroll_to_product(add_cart)
        self.tap_button(add_cart)

    def check_cart_value(self, value):
        cart_value = (AppiumBy.XPATH, "//android.widget.TextView[@text='" + value + "']")
        return self.is_element_displayed(cart_value)

    def navigate_to_cart_screen(self):
        self.is_element_displayed(self.cart_icon)
        self.tap_button(self.cart_icon)

