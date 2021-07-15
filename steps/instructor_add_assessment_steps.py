from behave import when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@when(u'The Instructor clicks on a Plus Assessment Button')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until(
            EC.element_to_be_clickable((By.ID, "addAssessmentBtn"))
        )
    except NoSuchElementException:
        assert False

    context.batch_home_page.add_assessment_button().click()


@when(u'The Instructor selects the assessment type {assessment_type}')
def step_impl(context, assessment_type: str):
    try:
        WebDriverWait(context.driver, 1).until(
            EC.element_to_be_clickable((By.ID, "assessment-type"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False
    select = Select(context.batch_home_page.assessment_type())

    if assessment_type == "QC":
        select.select_by_value('1')
    elif assessment_type == "Quiz":
        select.select_by_value('2')
    elif assessment_type == "One-on-Ones":
        select.select_by_value('3')
    elif assessment_type == "Project":
        select.select_by_value('4')


@when(u'The Instructor enters a name of {name} for the Assessment')
def step_impl(context, name: str):
    context.batch_home_page.assessment_title().send_keys(name)


@when(u'The Instructor clicks the button to create the Assessment')
def step_impl(context):
    context.batch_home_page.create_assessment_button().click()


# fails due to frontend functionality
@then(u'The list of Assessments for that week is updated with the new one ({name})')
def step_impl(context, name: str):
    context.batch_home_page.close_assessment_button().click()
    try:
        WebDriverWait(context.driver, 3).until(
            EC.text_to_be_present_in_element((By.ID, "week1Assessments"), name)
        )
    except (TimeoutException, NoSuchElementException):
        assert False
