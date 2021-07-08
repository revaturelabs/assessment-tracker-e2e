import os
import time
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@when('The User clicks on a batch {batch}')
def step_impl(context, batch: str):
    context.home_page.batch_button().click()


@then('The title should say {title}')
def step_impl(context, title: str):
    assert context.driver.title == title

@when(u'The User logs out')
def step_impl(context):
    context.home_page.login_button().click()
    context.home_page.logout_button().click()
