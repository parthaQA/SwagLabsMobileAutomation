from itertools import product

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

from screens.cart import Cart
from screens.checkout import Checkout
from screens.login import Login
from screens.products import Products
from utils.commonUtils import CommonUtils


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android", help="Platform: android or ios")

@pytest.fixture(scope="function")
def setup(request):
    options = AppiumOptions()
    device_os = request.config.getoption("--platform")
    if device_os == "android":
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Android",
            "appium:appPackage": "com.swaglabsmobileapp",
            "appium:appActivity": "MainActivity",
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "noReset": True
        })
    elif device_os == "ios":
        options.load_capabilities({
            "platformName": "ios",
        })
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    util = CommonUtils(driver)
    request.cls.util = util
    login = Login(driver)
    product = Products(driver)
    cart =  Cart(driver)
    checkout = Checkout(driver)
    request.cls.login = login
    request.cls.product = product
    request.cls.cart = cart
    request.cls.checkout = checkout
    request.cls.driver = driver
    try:
        yield driver
    finally:
        driver.terminate_app("com.swaglabsmobileapp")
