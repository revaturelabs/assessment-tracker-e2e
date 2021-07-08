# Legacy code, can be refactored at will

from selenium.webdriver.chrome.webdriver import WebDriver

# Variables for set_associate_scores_steps
test_1_name: str = '//*[@id="associate1"]/a'
test_1_assessment: str = "score18"
test_1_save: str = '//*[@id="GiveScoreForm18"]/div[2]/button[1]'

test_2_name: str = '//*[@id="associate11"]/a'
test_2_assessment: str = "score15"
test_2_save: str = '//*[@id="GiveScoreForm15"]/div[2]/button[1]'

test_3_name: str = '//*[@id="associate10"]/a'
test_3_assessment: str = "score16"
test_3_save: str = '//*[@id="GiveScoreForm16"]/div[2]/button[1]'

class BatchHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_assessment_button(self):
        return self.driver.find_element_by_id("addAssessmentBtn")

    def assessment_type(self):
        return self.driver.find_element_by_id("assessment-type")

    def assessment_title(self):
        return self.driver.find_element_by_id("assessment-title")

    def create_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[1]')

    def close_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[2]')

    # For set_associate_scores_steps
    def get_name_1(self):
        return self.driver.find_element_by_xpath(test_1_name)

    def get_name_2(self):
        return self.driver.find_element_by_xpath(test_2_name)

    def get_name_3(self):
        return self.driver.find_element_by_xpath(test_3_name)

    # For set_associate_scores_steps
    def set_grade_1(self):
        return self.driver.find_element_by_id(test_1_assessment)

    def set_grade_2(self):
        return self.driver.find_element_by_id(test_2_assessment)

    def set_grade_3(self):
        return self.driver.find_element_by_id(test_3_assessment)

    # For set_associate_scores_steps
    def save_button_1(self):
        return self.driver.find_element_by_xpath(test_1_save)

    def save_button_2(self):
        return self.driver.find_element_by_xpath(test_2_save)

    def save_button_3(self):
        return self.driver.find_element_by_xpath(test_3_save)
