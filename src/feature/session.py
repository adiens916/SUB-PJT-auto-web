import __init__
from src.core.login.page import LoginPage


def get_cookies(targets: set[str]) -> dict:
    login_page = LoginPage()
    login_page.login()

    cookies = login_page.get_cookies(keys=targets)
    return cookies


if __name__ == "__main__":
    targets = set(["WMONID", "JSESSIONID"])
    cookies = get_cookies(targets)
