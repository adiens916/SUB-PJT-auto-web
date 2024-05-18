import __init__
from src.base.custom_selenium.base_page import BasePage
from src.core.login.locators import *
from src.core.login.elements import URL
from account import ID, PW


class LoginPage(BasePage):
    def login(self):
        self.driver.get(URL)
        self.wait_to_load(login_button)

        self.find(account_id).send_keys(ID)
        self.find(account_pw).send_keys(PW)
        self.find(login_button).click()

        self.wait_to_load(menu_bar)
        self.driver.execute_script("window.stop();")
