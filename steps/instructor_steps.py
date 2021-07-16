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
            EC.presence_of_element_located((By.ID, "yearsWorked"))
        )
    # this code will only execute if the user is NOT logged in as an trainer (could be logged in as an admin or not
    # logged in at all)
    except TimeoutException:
        try:
            WebDriverWait(context.driver, 1).until(
                EC.presence_of_element_located((By.ID, "panels"))
            )
            # this code will only execute if the user is logged in as an admin
            context.home_page.logout_button().click()
            context.home_page.confirm_logout_button().click()
            instructor_login(context)
        # this code will only execute if the user IS NOT logged in as a trainer or an admin
        except TimeoutException:
            instructor_login(context)
    # final test to check if the user is logged in as a trainer
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.ID, "yearsWorked"))
        )
    except (NoSuchElementException, TimeoutException):
        assert False


def instructor_login(context):
    # this line fixes a bug I encountered where the https version of the site kept getting loaded for some reason,
    # which breaks the login function
    context.driver.get("http://adam-ranieri-batch-1019.s3-website-us-east-1.amazonaws.com/")
    context.home_page.login_button().click()
    context.driver.implicitly_wait(1)
    context.home_page.login_credentials().send_keys("rs@revature.com")
    # without this sleep function the login box will not disappear, DO NOT REMOVE
    sleep(1)
    context.home_page.login_cred_button().click()


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
