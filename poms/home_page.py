from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    login_cred_btn: str = '//*[@id="loginform"]/div[2]/div[2]/button[1]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "loginBtn")))

    def login_credentials(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "recipient-email")))

    def login_cred_button(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.login_cred_btn)))

    def logout_button(self):
        return self.driver.find_element_by_xpath('//*[@id="logoutModal"]/div/div/div[2]/div[2]/button[1]')

    def python_batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button[1]')

    def java_batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button[2]')

    def c_sharp_batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button[3]')

    def c_plus_plus_batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2021"]/button[1]')

    def ios_development_batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2021"]/button[2]')
