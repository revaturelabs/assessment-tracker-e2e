import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given('The User is on the home page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("URI")


@when('The User clicks on a batch {batch}')
def step_impl(context, batch: str):
    raise NotImplementedError(u'STEP: When The User clicks on a batch temp')


@then('The title should say {title}')
def step_impl(context, title: str):
    raise NotImplementedError(u'STEP: Then The title should say Assessment Tracker - Batches by Week')