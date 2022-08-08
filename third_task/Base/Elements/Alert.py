from third_task.resourses.singldriver import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from third_task.resourses.utils import random_string
from third_task.resourses.logger import log


class Alert:

    @staticmethod
    def switch_to_alert():
        try:
            return driver.switch_to.alert
        except TimeoutException:
            log().erroe('Cant switch to alert')
            return False

    @staticmethod
    def alert_is_present(timeout=3):
        try:
            WebDriverWait(driver, timeout).until(EC.alert_is_present())
            log().info('Alert is present')
            return True
        except TimeoutException:
            log().error('Alert is not present')
            return False

    @staticmethod
    def click_alert_ok():
        Alert.alert_is_present()
        alert = Alert.switch_to_alert()
        alert.accept()

    @staticmethod
    def check_alert_invis():
        return True if not Alert.alert_is_present() else False

    @staticmethod
    def alert_is_not_present():
        log().info('Alert dissmissed')
        driver.switch_to.alert.dismiss()

    @staticmethod
    def get_text():
        Alert.switch_to_alert()
        return driver.switch_to.alert.text

    @staticmethod
    def send_keys(text):
        alert = Alert.switch_to_alert()
        log().info('Try to send keys to alert')
        alert.send_keys(text)
