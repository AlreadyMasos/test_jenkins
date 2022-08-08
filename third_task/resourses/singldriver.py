from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as firefoxs
from selenium.webdriver.chrome.service import Service as chromes
from third_task.resourses.browser_factory import BrowserFactory


class WebDriver:

    _driver = None
    _factory = BrowserFactory()

    def __init__(self, browser_name='Chrome'):
        if not self._driver:
            if browser_name == 'Chrome':
                WebDriver._driver = self._factory.ChromeDriver()
                WebDriver._driver = WebDriver._driver.get_chrome()
            elif browser_name == 'Firefox':
                WebDriver._driver = self._factory.FirefoxDriver()
                WebDriver._driver = WebDriver._driver.get_fox()

    def get_driver(self):
        return self._driver


driver = WebDriver()
driver = driver.get_driver()

