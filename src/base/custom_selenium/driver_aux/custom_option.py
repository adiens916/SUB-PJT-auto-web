from selenium import webdriver


# Set option arguments for Chrome Driver
arguments = [
    "--no-first-run",
    "--no-service-autorun",
    "--password-store=basic",
]


class CustomOption(webdriver.ChromeOptions):
    def __init__(self, headless: bool) -> None:
        super().__init__()

        # Add arguments
        self.add_argument(" ".join(arguments))

        # Enable headless if it's wanted
        if headless:
            self.add_argument("headless=new")

        # Enable "execute_script" method before loading web page
        self.page_load_strategy = "none"
