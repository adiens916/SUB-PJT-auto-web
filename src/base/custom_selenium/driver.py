from .driver_aux.custom_driver import CustomWebDriver
from .driver_aux.custom_option import CustomOption


class Driver:
    @classmethod
    def get_chrome_driver(cls):
        driver = CustomWebDriver(options=CustomOption())
        return driver
