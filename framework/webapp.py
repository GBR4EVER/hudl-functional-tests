from selenium import webdriver
from resources.config import settings
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def __get__(self, instance, owner):
        if self.instance is None:
            self.instance = WebApp
        return self.instance

    def __init__(self):
        if str(settings['browser']).lower() is "firefox":
            self.driver = webdriver.Firefox()
        elif str(settings['browser']).lower() is "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def verify_nav_button_exists(self, component):
        assert component in self.driver.find_element_by_class_name('nav-button')
