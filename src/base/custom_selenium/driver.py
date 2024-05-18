from .driver_aux.custom_driver import CustomWebDriver
from .driver_aux.custom_option import CustomOption


class Driver:
    driver_dict = {}

    @classmethod
    def get_driver(
        cls, driver_num: int, driver_type: str = "Chrome"
    ) -> CustomWebDriver:
        """
        Get an instance of driver by the given number (ID).

        Args:
            driver_num: ID for driver instance
            driver_type: (default Chrome)

        Returns:
            CustomWebDriver
        """

        # Get a driver by the given number
        driver = cls.driver_dict.get(driver_num)

        # If any driver hasn't be created, create a new one.
        if driver is None:
            driver = cls.run_driver_by_type(cls, driver_type)
            cls.driver_dict.update({driver_num: driver})

        # Return the driver
        return driver

    def run_driver_by_type(cls, driver_type: str):
        if driver_type == "Chrome":
            driver = CustomWebDriver(options=CustomOption())
        return driver
