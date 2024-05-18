from selenium import webdriver


# Set option arguments for Chrome Driver
arguments = [
    "--no-first-run",
    "--no-service-autorun",
    "--password-store=basic",
]


class CustomOption(webdriver.ChromeOptions):
    def __init__(self) -> None:
        super().__init__()

        # Add arguments
        self.add_argument(" ".join(arguments))

        # Enable "execute_script" method before loading web page
        self.page_load_strategy = "none"
