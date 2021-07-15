from time import sleep
from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Successful Search'''


@when(u'The Instructor types {name} into the Search Bar')
def step_impl(context, name: str):
    context.nav_bar_page.search_bar().send_keys(name)


@then(u'A list of results is displayed beneath the Search Bar that includes {name}')
def step_impl(context, name: str):
    WebDriverWait(context.driver, 3).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/header/nav/div[2]/form/div/div[2]/div/a/strong"), name)
    )


@when(u'The Instructor clicks on the result {name}')
def step_impl(context, name: str):
    WebDriverWait(context.driver, 3).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/header/nav/div[2]/form/div/div[2]/div/a/strong"), name)
    )
    # Needed to ensure result is present on DOM
    sleep(0.5)
    context.nav_bar_page.search_row_one().click()


@then(u'They are taken to the page for that Batch')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(
        EC.title_is("Assessment Tracker - Batches by Week")
    )
    context.home_page.login_button().click()
    context.home_page.logout_button().click()
