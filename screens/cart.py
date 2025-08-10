from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from utils.commonUtils import CommonUtils


class Cart(CommonUtils):


    cart_screen = (AppiumBy.XPATH, "//android.widget.TextView[@text='YOUR CART']")
    cart_value = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Item']")
    remove_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='REMOVE']")
    checkout_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT']")
    price = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Price']/android.widget.TextView")

    def __init__(self, driver):
        super().__init__(driver)


    def verify_cart_screen(self):
        return self.is_element_displayed(self.cart_screen)

    def number_of_products_in_cart(self):
        self.is_element_displayed(self.cart_screen)
        cart_items = self.driver.find_elements(*self.cart_value)
        return cart_items

    def get_product_amount(self):
        return self.validate_text(self.price)


    def remove_product(self):
        self.is_element_displayed(self.cart_screen)
        cart_items = self.driver.find_elements(*self.cart_value)
        print("cart items", len(cart_items))
        for i in range(len(cart_items)):
            self.tap_button(self.remove_button)
            cart_items = self.driver.find_elements(*self.cart_value)
            if len(cart_items)==1:
                break
        try:
            self.driver.find_element(*self.cart_value)
        except NoSuchElementException:
            return True


    def navigate_to_checkout_screen(self):
        self.is_element_displayed(self.checkout_button)
        self.tap_button(self.checkout_button)
