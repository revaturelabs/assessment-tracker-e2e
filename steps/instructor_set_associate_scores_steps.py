import time

from behave import when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @when(u'The Instructor clicks on an Associate {name} from a list')
# def step_impl(context, name: str):
#     if name == "Zachary":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.get_name_1().click()
#     elif name == "Kerry":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.get_name_2().click()
#     elif name == "Patrick":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.get_name_3().click()


# @when(u'The Instructor sets a grade for an {assessment}')
# def step_impl(context, assessment: str):
#     if assessment == "TEST":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.set_grade_1().clear()
#         context.batch_home_page.set_grade_1().send_keys("100")
#     elif assessment == "iOS Quiz":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.set_grade_2().clear()
#         context.batch_home_page.set_grade_2().send_keys("70")
#     elif assessment == "Cumulative":
#         context.driver.implicitly_wait(3)
#         context.batch_home_page.set_grade_3().clear()
#         context.batch_home_page.set_grade_3().send_keys("20")


# @when(u'The Instructor clicks the {button} to save the Score')
# def step_impl(context, button):
#     if button == "save1":
#         context.batch_home_page.save_button_1().click()
#     elif button == "save2":
#         context.batch_home_page.save_button_2().click()
#     elif button == "save3":
#         context.batch_home_page.save_button_3().click()

@when(u'The Instructor clicks on an Associate {name} for the {assessment} assessment')
def step_impl(context, name, assessment):
    WebDriverWait(context.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr > th")))
    assessment_index = -1
    for i, a in enumerate(context.assessments_page.table_head()):
        if a.text == assessment:
            assessment_index = i 
    
    name_index = -1
    for i in range(len(context.assessments_page.table_rows()) - 1):
        if context.driver.find_element_by_id(f"associate-name-{i}").text == name:
            name_index = i

    context.driver.find_element_by_id(f"grade-data-{name_index}-{assessment_index - 1}").send_keys(42)

@when(u'The Instructor clicks the save score button')
def step_impl(context):
    context.assessments_page.save_grades_button().click()

@then(u'A message should tell the Instructor that their grade was saved')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(EC.alert_is_present())
        alert = context.driver.switch_to.alert
        alert.accept()
        assert True
    except TimeoutException:
        assert False
    finally:
        context.driver.get("http://adam-ranieri-batch-1019.s3-website-us-east-1.amazonaws.com/")
