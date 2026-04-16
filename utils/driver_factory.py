from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            return webdriver.Chrome(options=options)

        raise Exception("Unsupported browser")