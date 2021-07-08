# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver

# Variables for set_associate_scores_steps
test_1_batch: str = '//*[@id="batch_2020"]/button[1]'

test_2_batch: str = '//*[@id="batch_2021"]/button[2]'

test_3_batch: str = '//*[@id="batch_2021"]/button[1]'

class HomePage:

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
        return self.driver.find_element_by_xpath('//*[@id="batch_2020"]/button')

    # For set_associate_scores_steps
    # access the first button under a 2020 batch card
    def batch_button_1(self):
        return self.driver.find_element_by_xpath(test_1_batch)

    # access the second button under a 2021 batch card
    def batch_button_2(self):
        return self.driver.find_element_by_xpath(test_2_batch)

    # access the first button under a 2021 batch card
    def batch_button_3(self):
        return self.driver.find_element_by_xpath(test_3_batch)
