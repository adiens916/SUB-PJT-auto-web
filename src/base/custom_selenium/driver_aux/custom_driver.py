from selenium import webdriver
from selenium.webdriver.common.by import By

from .custom_element import CustomWebElement


class CustomWebDriver(webdriver.Chrome):
    _web_element_cls = CustomWebElement

    def find_element(self, by=By.ID, value: str | None = None) -> CustomWebElement:
        return super().find_element(by, value)
