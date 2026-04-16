import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # element fetch
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Actions with retry
    def click(self, locator, retries=2):
        for i in range(retries):
            try:
                self.find_clickable(locator).click()
                return
            except Exception as e:
                Logger.error(f"Click retry {i + 1} failed: {e}")
                if i == retries - 1:
                    self.take_screenshot("click_failure")
                    raise
                time.sleep(1)

    # send keys
    def send_keys(self, locator, value, retries=2):
        for i in range(retries):
            try:
                el = self.find_visible(locator)
                el.clear()
                el.send_keys(value)
                return
            except Exception as e:
                Logger.error(f"Send_keys retry {i + 1} failed: {e}")
                if i == retries - 1:
                    self.take_screenshot("sendkeys_failure")
                    raise
                time.sleep(1)

    def get_text(self, locator):
        return self.find_visible(locator).text

    # Screenshot
    def take_screenshot(self, name):
        path = f"reports/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(path)
        Logger.info(f"Screenshot saved: {path}")
