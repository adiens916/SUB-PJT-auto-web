from module.common.web.activator import Driver
from page import LoginPage


def main():
    driver = Driver().get_chrome_driver()
    LoginPage(driver).login()


if __name__ == "__main__":
    main()
