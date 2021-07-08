from time import sleep
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''Successful Search'''
@given(u'The User is logged in as an Instructor')
def step_impl(context):
    context.driver.get("http://18.224.184.27:5000/home")
    context.home_page.login_button().click()
    context.driver.implicitly_wait(10)
    context.home_page.login_credentials().send_keys("rs@revature.com")
    # without this sleep function the login box will not disappear, DO NOT REMOVE
    sleep(1)
    context.home_page.login_cred_button().click()
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "trainerName"))
        )
    except NoSuchElementException:
        assert False

@when(u'The Instructor types {name} into the Search Bar')
def step_impl(context, name: str):
    context.nav_bar_page.search_bar().send_keys(name)

@then(u'A list of results is displayed beneath the Search Bar that includes {name}')
def step_impl(context, name: str):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/header/nav/div[2]/form/div/div[2]/div/a/strong"), name)
    )

@when(u'The Instructor clicks on the result {name}')
def step_impl(context, name: str):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/header/nav/div[2]/form/div/div[2]/div/a/strong"), name)
    )
    # Needed to ensure result is present on DOM
    sleep(0.5)
    context.nav_bar_page.search_row_one().click()

@then(u'They are taken to the page for that Batch')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.title_is("Assessment Tracker - Batches by Week")
    )
    context.home_page.login_button().click()
    context.home_page.logout_button().click()
