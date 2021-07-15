from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "loginBtn")))

    def login_credentials(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))

    def login_cred_button(self):
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "login_cred_button")))

    def logout_button(self):
        return self.driver.find_element_by_id("loginBtn")

    def confirm_logout_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By. ID, "logout_button")))

    def python_batch_button(self):
        return self.driver.find_element_by_css_selector("button[onclick*='1']")

    def java_batch_button(self):
        return self.driver.find_element_by_css_selector("button[onclick*='3']")

    def c_sharp_batch_button(self):
        return self.driver.find_element_by_css_selector("button[onclick*='4']")

    def c_plus_plus_batch_button(self):
        return self.driver.find_element_by_css_selector("button[onclick*='5']")

    def ios_development_batch_button(self):
        return self.driver.find_element_by_css_selector("button[onclick*='6']")
