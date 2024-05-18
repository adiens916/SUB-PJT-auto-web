from selenium import webdriver
from selenium.webdriver.common.by import By
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


class CustomWebDriver(webdriver.Chrome):
    _web_element_cls = CustomWebElement

    def find_element(self, by=By.ID, value: str | None = None) -> CustomWebElement:
        return super().find_element(by, value)


class Driver:
    @classmethod
    def get_chrome_driver(cls):
        # driver = webdriver.Chrome(options=cls.__get_options(cls))
        driver = CustomWebDriver(options=cls.__get_options(cls))
        return driver

    def __get_options(self):
        # 크롬 드라이버 옵션 설정
        arguments = ["--no-first-run", "--no-service-autorun", "--password-store=basic"]

        options = webdriver.ChromeOptions()
        options.add_argument(" ".join(arguments))
        options.page_load_strategy = "none"  # 페이지가 전부 로딩되기 전에도 execute_script 가능
        return options
