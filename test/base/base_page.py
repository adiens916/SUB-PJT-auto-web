import unittest

import __init__
from src.base.custom_selenium.base_page import BasePage


class BasePageTest(unittest.TestCase):
    def test_get_driver(self):
        # [given]
        base_page_1 = BasePage()

        # [when]
        base_page_2 = BasePage()

        # [then] pages aren't equal, but drivers are the same.
        self.assertIsNot(base_page_1, base_page_2)
        self.assertIs(base_page_1.driver, base_page_2.driver)


if __name__ == "__main__":
    unittest.main(defaultTest="BasePageTest")
