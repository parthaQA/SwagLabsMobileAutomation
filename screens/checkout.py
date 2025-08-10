from appium.webdriver.common.appiumby import AppiumBy
from utils.commonUtils import CommonUtils


class Checkout(CommonUtils):


    checkout_screen = (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT: INFORMATION']")
    first_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
    last_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
    postal_code_field = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
    continue_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='CONTINUE']")
    checkout_overiew_screen = (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT: OVERVIEW']")
    finish_button = (AppiumBy.XPATH, "//android.widget.TextView[@text='FINISH']")
    cancel_button = (AppiumBy.ACCESSIBILITY_ID, "test-CANCEL")
    gt_price = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Price']/android.widget.TextView")
    frist_name_error = (AppiumBy.XPATH, "//android.widget.TextView[@text='First Name is required']")
    checkout_complete_screen = (AppiumBy.XPATH, "//android.widget.TextView[@text='CHECKOUT: COMPLETE!']")
    order_success = (AppiumBy.XPATH, "//android.widget.TextView[@text='THANK YOU FOR YOU ORDER']")



    def __init__(self, driver):
        super().__init__(driver)


    def verify_checkout_screen(self):
        return self.is_element_displayed(self.checkout_screen)

    def enter_first_name(self, firstname):
        self.is_element_displayed(self.first_name_field)
        self.enter_text(self.first_name_field,firstname)

    def enter_last_name(self, lastname):
        self.is_element_displayed(self.last_name_field)
        self.enter_text(self.last_name_field,lastname)

    def enter_postal_code(self, postal_code):
        self.is_element_displayed(self.postal_code_field)
        self.enter_text(self.postal_code_field, postal_code)

    def tap_continue_button(self):
        self.tap_button(self.continue_button)

    def verify_checkout_overview_screen(self):
        return self.is_element_displayed(self.checkout_overiew_screen)

    def product_information(self, product_name):
        prod_name = (AppiumBy.XPATH, "//android.widget.TextView[@text='" + product_name + "']")
        return self.is_element_displayed(prod_name)

    def product_price(self, price):
        prod_price = (AppiumBy.XPATH, "//android.widget.TextView[@text='" + price + "']")
        return self.is_element_displayed(prod_price)


    def tap_on_finish_button(self):
        self.scroll_to_product(self.finish_button)
        self.tap_button(self.finish_button)

    def tap_on_cancel_button(self):
        self.scroll_to_product(self.cancel_button)
        self.tap_button(self.cancel_button)

    def first_name_error_message(self):
        return self.is_element_displayed(self.frist_name_error)

    def get_successful_purchase(self):
        self.is_element_displayed(self.checkout_complete_screen)
        return self.is_element_displayed(self.order_success)