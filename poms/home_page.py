# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    batch_btn1: str = '//*[@id="batch_2020"]/button'
    batch_btn2: str = '//*[@id="batch_2020"]/button[2]'
    login_cred_btn: str = '//*[@id="loginform"]/div[2]/div[2]/button[1]'

    # Variables for set_associate_scores_steps
    test_1_batch: str = '//*[@id="batch_2020"]/button[1]'
    test_2_batch: str = '//*[@id="batch_2021"]/button[2]'
    test_3_batch: str = '//*[@id="batch_2021"]/button[1]'

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

    # The button for a user to click on to view that specific batches information
    def batch_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, self.batch_btn1)))

    # return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button')
    # return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.batch_btn)))

    # For set_associate_scores_steps
    # access the first button under a 2020 batch card
    def batch_button_1(self):
        return self.driver.find_element_by_xpath(self.test_1_batch)

    # access the second button under a 2021 batch card
    def batch_button_2(self):
        return self.driver.find_element_by_xpath(self.test_2_batch)

    # access the first button under a 2021 batch card
    def batch_button_3(self):
        return self.driver.find_element_by_xpath(self.test_3_batch)
