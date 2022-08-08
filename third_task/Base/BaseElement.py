from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from third_task.resourses.singldriver import driver
from third_task.resourses.logger import log
import logging


class BaseElement:
    logs = log(logging.DEBUG)

    def __init__(self, locator_name, locator_type='xpath'):
        self.locator_name = locator_name
        self.locator_type = locator_type

    def find_element(self):
        self.logs.info('Element found')
        return driver.find_element(self.locator_type, self.locator_name)

    def find_elements(self):
        self.logs.info('list of elements found')
        return list(driver.find_elements(self.locator_type, self.locator_name))

    def element_click(self):
        self.find_element().click()

    def wait_until_loaded(self, wait_time=3):
        try:
            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((self.locator_type, self.locator_name)))
        except TimeoutException:
            self.logs.exception('TimeoutException when try to wait for element')
