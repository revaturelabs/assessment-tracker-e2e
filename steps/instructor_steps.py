from time import sleep
from behave import given, when
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'The User is logged in as an Instructor')
def step_impl(context):
    context.driver.get("http://adam-ranieri-batch-1019.s3-website-us-east-1.amazonaws.com/")
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "trainerName"))
        )
    except TimeoutException:
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

        
@given(u'The Instructor is on a page for a {batch} batch')
def step_impl(context, batch: str):
    try:
        WebDriverWait(context.driver, 3).until(
            EC.text_to_be_present_in_element((By.ID, "batch_2020"), "2")
        )
    except NoSuchElementException:
        assert False

    if batch == "Python":
        context.home_page.python_batch_button().click()
    elif batch == "Java":
        context.home_page.java_batch_button().click()
    elif batch == "C#":
        context.home_page.c_sharp_batch_button().click()
    elif batch == "C++":
        context.home_page.c_plus_plus_batch_button().click()
    elif batch == "iOS Development":
        context.home_page.ios_development_batch_button().click()
    else:
        assert False
    try:
        WebDriverWait(context.driver, 5).until(
            EC.title_is("Assessment Tracker - Batches by Week")
        )
    except NoSuchElementException:
        assert False
