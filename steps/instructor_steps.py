from time import sleep
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'The Instructor is on a page for a Batch')
def step_impl(context):
    context.home_page.batch_button().click()
    try:
        WebDriverWait(context.driver, 1).until(
            EC.title_is("Assessment Tracker - Batches by Week")
        )
    except NoSuchElementException:
        assert False


@when(u'The Instructor clicks on a Plus Assessment Button')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(
            EC.element_to_be_clickable((By.ID, "addAssessmentBtn"))
        )
    except NoSuchElementException:
        assert False

    context.batch_home_page.add_assessment_button().click()


@when(u'The Instructor selects an Assessment Type')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(
            EC.element_to_be_clickable((By.ID, "assessment-type"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False
    select = Select(context.batch_home_page.assessment_type())
    select.select_by_value('1')


@when(u'The Instructor enters a name for the Assessment')
def step_impl(context):
    context.batch_home_page.assessment_title().send_keys("Selenium Quiz")


@when(u'The Instructor clicks the button to create the Assessment')
def step_impl(context):
    context.batch_home_page.create_assessment_button().click()


@then(u'The list of Assessments for that week is updated with the new one')
def step_impl(context):
    context.batch_home_page.close_assessment_button().click()
    try:
        WebDriverWait(context.driver, 1).until(
            EC.text_to_be_present_in_element((By.ID, "week1Assessments"), "Selenium Quiz")
        )
    except (TimeoutException, NoSuchElementException):
        assert False
