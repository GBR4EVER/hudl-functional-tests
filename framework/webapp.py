from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def load_website(self):
        self.driver.get('https://hudl.com/login')

    def select_login(self):
        self.driver.find_element_by_class_name('nav-button')

    def verify_nav_button_exists(self):
        # noinspection PyBroadException
        try:
            assert self.driver.find_element_by_class_name('btn__blue login')
        except:
            print("Unable to locate navigation login button.")

    def click_nav_login(self):
        try:
            element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn__blue login")))
            nav_login_button = self.driver.find_element_by_xpath(element)
            nav_login_button.click()
        except:
            print("Cannot find nav login.")

    def input_credentials(self):
        username = self.driver.find_element_by_id('email')
        username.send_keys('burkleycorey@yahoo.com')
        password = self.driver.find_element_by_id('password')
        password.send_keys('GBR4EVER')

    def input_invalid_credentials(self):
        username = self.driver.find_element_by_id('email')
        username.send_keys('test')

    def click_remember_password(self):
        remember_button = self.driver.find_element_by_id('remember-me')
        remember_button.click()

    def click_login(self):
        login_button = self.driver.find_element_by_id('logIn')
        login_button.click()

    def verify_user_logged_in(self):
        login_button = self.driver.find_element_by_id('logIn')
        assert login_button is None

    def verify_login_error(self):
        login_error = self.driver.find_element_by_xpath('/html/body/div[2]/form[1]/div[3]')
        assert login_error
        self.driver.quit()

    def verify_coach_page(self):
        try:
            assert self.driver.current_url("https://www.hudl.com/home")
        except:
            print("User not successfully routed to home page.")

        # TODO Need to determine how to quit Webdriver properly.
        # try:
        #     self.driver.close()
        # except:
        #     print("Unable to close the Webdriver.")


webapp = WebApp.get_instance()
