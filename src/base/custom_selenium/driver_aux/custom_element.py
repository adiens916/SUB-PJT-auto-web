from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class CustomWebElement(WebElement):
    def click_by_script(self) -> None:
        self.parent: webdriver.Chrome
        self.parent.execute_script("arguments[0].click();", self)

    def clear_by_script(self) -> None:
        self.parent: webdriver.Chrome
        self.parent.execute_script("arguments[0].value='';", self)

    def send_keys_by_script(self, value) -> None:
        self.parent: webdriver.Chrome
        self.parent.execute_script(f"arguments[0].value='{value}';", self)

    def scroll_into_view(self) -> None:
        self.parent: webdriver.Chrome
        self.parent.execute_script("arguments[0].scrollIntoView(true);", self)

    def find_element(self, locator: tuple[str, str]) -> "CustomWebElement":
        return super().find_element(by=locator[0], value=locator[1])
