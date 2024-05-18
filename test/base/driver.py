import unittest

import __init__
from src.base.custom_selenium.driver import Driver


class DriverTest(unittest.TestCase):
    def test_get_driver(self):
        # [given]
        driver_1 = Driver.get_driver(0)

        # [when]
        driver_2 = Driver.get_driver(0)

        # [then]
        self.assertIs(driver_1, driver_2)

    def test_get_multiple_driver(self):
        # [given]
        driver_1 = Driver.get_driver(1)
        driver_2 = Driver.get_driver(2)

        # [when]

        # [then]


if __name__ == "__main__":
    unittest.main(defaultTest="DriverTest.test_get_driver")
