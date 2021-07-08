# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BatchHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_assessment_button(self):
        return self.driver.find_element_by_id("addAssessmentBtn")

    def assessment_type(self):
        return self.driver.find_element_by_id("assessment-type")

    def assessment_title(self):
        return self.driver.find_element_by_id("assessment-title")

    def week1_assessment_btn(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='assessment_18']")))

    def create_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[1]')

    def close_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[2]')

    def adjust_weight_modal(self):
        return self.driver.find_element_by_id("adjustWeightModal")

    def adjust_weight_modal_hidden(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.invisibility_of_element((By.ID, "adjustWeightModal")))

    def weight_slider(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.ID,"weightControl")))

    def slider_submit_btn(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="adjustWeightForm"]/div[2]/button[1]')))