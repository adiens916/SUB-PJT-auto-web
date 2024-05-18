import unittest

import __init__
from src.core.login.page import LoginPage
from src.core.login.locators import next_page_element
from account import ID, PW


class LoginPageTest(unittest.TestCase):
    def test_login(self):
        # [given]
        login_page = LoginPage()
        # Ensure that account.py exists and ID & PW are not empty
        self.assertNotEqual(ID, "")
        self.assertNotEqual(PW, "")

        # [when] login www.naver.com
        login_page.login()

        # [then] next page has been loaded
        elem = login_page.find(next_page_element)
        self.assertIsNotNone(elem)


if __name__ == "__main__":
    unittest.main()
