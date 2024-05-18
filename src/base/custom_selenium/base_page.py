from typing import Callable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .driver_aux.custom_driver import CustomWebDriver
from .driver_aux.custom_element import CustomWebElement


class BasePage:
    def __init__(self, driver: CustomWebDriver):
        self.driver = driver
        # 명시적 대기 시 최대 5초간 대기
        self.wait = WebDriverWait(self.driver, 5)

    def find(self, locator: tuple[str, str]) -> CustomWebElement:
        """
        원하는 Web Element를 찾습니다.

        없으면 오류를 내는 대신에 None을 반환합니다.
        """
        # https://stackoverflow.com/questions/9567069/checking-if-element-exists-with-python-selenium
        try:
            specifier = locator[0]
            value = locator[1]

            element = self.driver.find_element(specifier, value)
            return element

        except NoSuchElementException:
            print(f"오류: 다음 요소를 찾을 수 없음 - {locator[1]}")
            return None

    def find_several(self, locator: tuple[str, str]) -> list[CustomWebElement]:
        """
        원하는 Web Element 여러 개를 찾습니다.

        없으면 오류를 내는 대신에 None을 반환합니다.
        """
        try:
            specifier = locator[0]
            value = locator[1]

            elements = self.driver.find_elements(specifier, value)
            return elements

        except NoSuchElementException:
            print(f"오류: 다음 요소를 찾을 수 없음 - {locator[1]}")
            return None

    def move_to(self, target_title: str):
        # https://www.selenium.dev/documentation/webdriver/browser_manipulation/

        # Wait for the new window or tab
        self.wait.until(EC.number_of_windows_to_be(2))

        # Store the ID of the original window
        # window_handle은 브라우저 타이틀 X => 아래와 같은 고유 ID를 가짐
        # e.g.) CDwindow-5B3C6A7CFB7405E93DF9899E9AF87311
        original_window = self.driver.current_window_handle

        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)

                # Wait for the new tab to finish loading content
                # self.wait.until(EC.title_is("SeleniumHQ Browser Automation"))

                # 추가: 원하는 페이지 타이틀이 포함되어 있나 확인
                if target_title in self.driver.title:
                    return

        print("No such title:", target_title)

    def wait_to_load(self, locator: tuple[str, str]):
        """해당 요소가 페이지의 DOM에 있는지 확인합니다."""
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_to_click(self, locator: tuple[str, str]):
        """해당 요소가 클릭이 가능한지 확인합니다."""
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_to_see(self, locator: tuple[str, str]):
        """해당 요소가 페이지에서 보이는지 확인합니다."""
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_to_disappear(self, locator: tuple[str, str]):
        """해당 요소가 페이지에서 보이지 않게 될 때까지 기다립니다."""
        self.wait.until(self.__element_display_property_is_none(locator))

    def __element_display_property_is_none(
        self, locator: CustomWebElement
    ) -> Callable[[CustomWebDriver], bool]:
        def _predicate(driver: CustomWebDriver):
            target = self.find(locator)
            if target is None:
                return True

            display = target.value_of_css_property("display")
            return "none" in display

        return _predicate
