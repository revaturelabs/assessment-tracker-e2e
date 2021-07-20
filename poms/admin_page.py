from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class AdminPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def batch_name_input(self):
        return self.driver.find_element_by_id("nameInput")

    def training_track_input(self):
        return self.driver.find_element_by_id('trackInput')

    def start_date_input(self):
        return self.driver.find_element_by_id('startDate')

    def end_date_input(self):
        return self.driver.find_element_by_id('endDate')

    def trainer_input(self):
        return Select(self.driver.find_element_by_id('batchTrainer'))

    def co_trainer_input(self):
        return Select(self.driver.find_element_by_id('batchCoTrainer'))

    def search_associate_input(self):
        return self.driver.find_element_by_id('searchAssociate')

    def unadded_associates(self):
        list_holder = self.driver.find_element_by_id('unaddedAssociates')
        return list_holder.find_elements_by_class_name('associateList')

    def added_associates(self):
        list_holder = self.driver.find_element_by_id('addedAssociates')
        return list_holder.find_elements_by_class_name('associateList')

    def create_associate_button(self):
        return self.driver.find_element_by_id('createAssociate')

    def submit_batch_button(self):
        return self.driver.find_element_by_id('submitBatch')

    def associate_email_input(self):
        return self.driver.find_element_by_id('emailInput')

    def associate_first_name_input(self):
        return self.driver.find_element_by_id('firstNameInput')

    def associate_last_name_input(self):
        return self.driver.find_element_by_id('lastNameInput')

    def cancel_new_associate_button(self):
        return self.driver.find_element_by_id('cancelAddButton')

    def submit_new_associate_button(self):
        return self.driver.find_element_by_id('submitAddButton')

    def view_averages_button(self):
        return self.driver.find_element_by_id('assessmentsBtn')
