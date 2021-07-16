from time import sleep
from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'The User clicks the create associate button')
def step_impl(context):
    create_button = context.admin_page.create_associate_button()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    create_button.click()

@then(u'The new associate popup should appear')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until(EC.visibility_of_element_located((By.ID, 'newAssociateModal')))
        assert True
    except TimeoutException:
        assert False


@when(u'The User enters an email for the new associate')
def step_impl(context):
    context.admin_page.associate_email_input().send_keys("selenium@automation.test")


@when(u'The User enters a first name for the new associate')
def step_impl(context):
    context.admin_page.associate_first_name_input().send_keys("Selenium")


@when(u'The User enters a last name for the new associate')
def step_impl(context):
    context.admin_page.associate_last_name_input().send_keys("Tests")


@when(u'The User selects the submit new associate button')
def step_impl(context):
    context.admin_page.submit_new_associate_button().click()


@then(u'The new associate popup should dissapear')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until(EC.invisibility_of_element_located((By.ID, 'newAssociateModal')))
        assert True
    except TimeoutException:
        assert False


@then(u'The new User should appear in the list of associates')
def step_impl(context):
    assert context.admin_page.unadded_associates()[-1].text == "Selenium Tests"


@when(u'The User selects the cancel new associate button')
def step_impl(context):
    context.admin_page.cancel_new_associate_button().click()


@then(u'A message should appear indicating the provided email is invalid')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, "invalid-feedback")))
        assert True
    except TimeoutException:
        assert False