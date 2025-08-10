import inspect
import logging
from faker.proxy import Faker
from pathlib import Path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonUtils:
    ROOT_DIR = Path(__file__).parent.parent

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.actions = ActionChains(self.driver)


    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_button_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


    def enter_text(self, locator, text):
        self.wait_for_element_visible(locator).send_keys(text)

    def is_element_displayed(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.is_displayed()

    def is_element_enabled(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.is_enabled()

    def validate_text(self, locator):
        element = self.wait_for_element_visible(locator)
        self.get_logger().info(f"{element.text} is found")
        return element.text


    def tap_button(self, locator):
        self.wait_for_button_clickable(locator).click()

    @staticmethod
    def generate_fake_candidate_data():
        faker = Faker()
        candidate_data = {
            "username": faker.first_name(),
            "lastname": faker.last_name(),
            "password": faker.password(),
            "postalcode": faker.postalcode()
        }
        return candidate_data

    @staticmethod
    def get_logger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(CommonUtils.ROOT_DIR / 'log' / 'logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.addHandler(fileHandler)
        return logger

    def scroll_to_product(self, locator):
        self.actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        window_size = self.driver.get_window_size()
        start_x = window_size['width'] // 2
        start_y = int(window_size['height'] * 0.5)
        end_y = int(window_size['height'] * 0.2)

        for _ in range(3):
            try:
                return self.is_element_displayed(locator)
            except:
                # Perform vertical scroll
                self.actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
                self.actions.w3c_actions.pointer_action.pointer_down()
                self.actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)
                self.actions.w3c_actions.pointer_action.release()
                self.actions.perform()
        self.get_logger().info("Element not found after scrolling.")
        return None


    def element_disappears(self, locator):
        return self.driver.find_element(locator)
