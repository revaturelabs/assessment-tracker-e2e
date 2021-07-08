import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given('The User is on the home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("http://34.204.173.118:5000/home")


@when('The User clicks on a batch {batch}')
def step_impl(context, batch: str):
    context.home_page.batch_button().click()


@then('The title should say {title}')
def step_impl(context, title: str):
    assert context.driver.title == str