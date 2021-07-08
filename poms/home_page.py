# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button(self):
        return self.driver.find_element_by_id("loginBtn")

    def login_credentials(self):
        return self.driver.find_element_by_id("recipient-email")

    def login_cred_button(self):
        return self.driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button[1]')

    def logout_button(self):
        return self.driver.find_element_by_xpath('//*[@id="logoutModal"]/div/div/div[2]/div[2]/button[1]')

    # The button for a user to click on to view that specific batches information
    def batch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button')
