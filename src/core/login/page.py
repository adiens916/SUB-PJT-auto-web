from base.custom_selenium.driver import CustomWebDriver
from base.custom_selenium.base_page import BasePage
from login.locators import *
from login.elements import URL
from account import ID, PW


class LoginPage(BasePage):
    def __init__(self, driver: CustomWebDriver):
        super().__init__(driver)
        self.driver.get(URL)

    def login(self):
        self.wait_to_load(login_button)

        self.find(account_id).send_keys(ID)
        self.find(account_pw).send_keys(PW)
        self.find(login_button).click()

        self.wait_to_load(menu_bar)
        self.driver.execute_script("window.stop();")
