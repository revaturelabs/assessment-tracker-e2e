# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    batch_btn: str = '//*[@id="batch_2020"]/button'
    login_cred_btn: str = '//*[@id="loginform"]/div[2]/div[2]/button[1]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "loginBtn")))

    def login_credentials(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "recipient-email")))

    def login_cred_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.login_cred_btn)))

    # The button for a user to click on to view that specific batches information
    def batch_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.batch_btn)))
