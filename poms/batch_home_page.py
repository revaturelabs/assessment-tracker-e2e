from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variables for set_associate_scores_steps
test_1_selec: str = "button[onclick*='1']"
test_1_assessment: str = "score224"
test_1_save: str = '//*[@id="GiveScoreForm222"]/div[2]/button[1]'

test_2_selec: str = "button[onclick*='6']"
test_2_assessment: str = "score15"
test_2_save: str = '//*[@id="GiveScoreForm15"]/div[2]/button[1]'

test_3_selec: str = "button[onclick*='5']"
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

    def week1_assessment_btn(self):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[onclick*='.assessment']")))

    def create_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[1]')

    def close_assessment_button(self):
        return self.driver.find_element_by_xpath('//*[@id="createAssessmentForm"]/div[4]/button[2]')

    def adjust_weight_modal(self):
        return self.driver.find_element_by_id("adjustWeightModal")

    def adjust_weight_modal_hidden(self):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.invisibility_of_element((By.ID, "adjustWeightModal")))

    def weight_slider(self):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.visibility_of_element_located((By.ID, "weightControl")))

    def slider_submit_btn(self):
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="adjustWeightForm"]/div[2]/button[1]')))

    def get_name_1(self):
        return self.driver.find_element_by_css_selector(test_1_selec)

    def get_name_2(self):
        return self.driver.find_element_by_css_selector(test_2_selec)

    def get_name_3(self):
        return self.driver.find_element_by_css_selector(test_3_selec)

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
