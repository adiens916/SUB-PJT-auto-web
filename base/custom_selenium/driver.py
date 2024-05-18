from selenium import webdriver

from driver_aux.custom_driver import CustomWebDriver


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
        options.page_load_strategy = (
            "none"  # 페이지가 전부 로딩되기 전에도 execute_script 가능
        )
        return options
