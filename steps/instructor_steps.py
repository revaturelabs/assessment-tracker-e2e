from time import sleep

from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'The User is logged in as an Instructor')
def step_impl(context):
    context.driver.get("http://34.204.173.118:5000/home")
    context.home_page.login_button().click()
    context.driver.implicitly_wait(1)
    context.home_page.login_credentials().send_keys("rs@revature.com")
    # without this sleep function the login box will not disappear, DO NOT REMOVE
    sleep(1)
    context.home_page.login_cred_button().click()
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "trainerName"))
        )
    except NoSuchElementException:
        assert False


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
    raise NotImplementedError(u'STEP: When The Instructor clicks on a Plus Assessment Button')


@when(u'The Instructor selects an Assessment Type')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor selects an Assessment Type')


@when(u'The Instructor enters a name for the Assessment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor enters a name for the Assessment')


@when(u'The Instructor clicks the button to create the Assessment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor clicks the button to create the Assessment')


@then(u'The list of Assessments for that week is updated with the new one')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The list of Assessments for that week is updated with the new one')
