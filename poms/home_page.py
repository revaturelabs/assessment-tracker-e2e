# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    batch_btn1: str = '//*[@id="batch_2020"]/button'
    batch_btn2: str = '//*[@id="batch_2020"]/button[2]'
    login_cred_btn: str = '//*[@id="loginform"]/div[2]/div[2]/button[1]'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return self.driver.find_element_by_id("loginBtn")

    def login_credentials(self):
        return self.driver.find_element_by_id("recipient-email")

    def login_cred_button(self):
        return self.driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button[1]')

    # def batch_button(self):
    #     return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button')

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

    def batch_button(self, html_id: str):
        if html_id == "temp":
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.batch_btn1)))
        if html_id == "temp2":
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.batch_btn2)))

