from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UploadPage(BasePage):

    # locators
    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")

    # actions
    def upload_file(self, file_path):
        self.send_keys(self.FILE_UPLOAD, file_path)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)