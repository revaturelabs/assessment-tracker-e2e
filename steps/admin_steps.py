from time import sleep
from behave import given
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'The User is logged in as an Admin')
def step_impl(context):
    context.driver.get("http://adam-ranieri-batch-1019.s3-website-us-east-1.amazonaws.com/")
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.ID, "panels"))
        )
    # this code will only execute if the user is NOT logged in as an admin (could be logged in as a trainer or not
    # logged in at all)
    except TimeoutException:
        try:
            WebDriverWait(context.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "trainerName"))
            )
            # this code will only execute if the user is logged in as a trainer
            context.home_page.logout_button().click()
            context.home_page.confirm_logout_button.click()
            admin_login(context)
        # this code will only execute if the user IS NOT logged in as a trainer or an admin
        except TimeoutException:
            admin_login(context)
    # final test to check if the user is logged in as an admin
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.ID, "panels"))
        )
    except NoSuchElementException:
        assert False


def admin_login(context):
    context.home_page.login_button().click()
    context.driver.implicitly_wait(1)
    context.home_page.login_credentials().send_keys("admin@revature.com")
    # without this sleep function the login box will not disappear, DO NOT REMOVE
    sleep(1)
    context.home_page.login_cred_button().click()
