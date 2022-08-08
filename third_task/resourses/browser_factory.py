from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as firefoxs
from selenium.webdriver.chrome.service import Service as chromes


class BrowserFactory:
    class ChromeDriver:
        service = chromes(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")

        def __init__(self):
            self._driver = webdriver.Chrome(service=self.service, options=self.options)

        def get_chrome(self):
            return self._driver

    class FirefoxDriver:
        service = firefoxs(GeckoDriverManager().install())
        options = webdriver.FirefoxProfile()
        options.set_preference("browser.privatebrowsing.autostart", True)

        def __init__(self):
            self._driver = webdriver.Firefox(service=self.service, firefox_profile=self.options)

        def get_fox(self):
            return self._driver
