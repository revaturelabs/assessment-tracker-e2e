# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver


class AssessmentsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def created_assessment(self):
        return self.driver.find_element_by_xpath('//*[@id="assessment_9"]')

    def grade_slider(self):
        return self.driver.find_element_by_id('weightControl')

    def grade_weight_save(self):
        return self.driver.find_element_by_css_selector('#adjustWeightForm > div.modal-footer > button.btn.btn-info')
