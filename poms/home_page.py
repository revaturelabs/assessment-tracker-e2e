# Legacy code, can be refactored at will
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    path1: str = '//*[@id="batch_2020"]/button'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return self.driver.find_element_by_id("loginBtn")

    def login_credentials(self):
        return self.driver.find_element_by_id("recipient-email")

    def login_cred_button(self):
        return self.driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button[1]')

    # The button for a user to click on to view that specific batches information
    def batch_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.path1)))