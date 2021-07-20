from time import sleep

from behave import when, then
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

note_to_add = "Study more about Selenium"


@when(u'The Instructor selects week number {number}')
def step_impl(context, number: int):
    select = Select(context.batch_home_page.week_select())
    select.select_by_value(number)


@when(u'The Instructor clicks on an associate\'s name')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 3).until(
            EC.element_to_be_clickable((By.ID, "associate-name-0"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False
    context.batch_home_page.associate_name().click()


@then(u'A popup appears where the Instructor can add or edit a note')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-dialog"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False


@then(u'The Instructor adds their note')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((By.ID, "note_text"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False
    sleep(.5)
    context.batch_home_page.notes_box().click()
    sleep(.5)
    context.batch_home_page.notes_box().clear()
    sleep(.5)
    context.batch_home_page.notes_box().send_keys(note_to_add)
    sleep(.5)


@then(u'The Instructor clicks Create')
def step_impl(context):
    context.batch_home_page.submit_notes().click()


@then(u'The new note is saved')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 2).until(
            EC.element_to_be_clickable((By.ID, "associate-name-0"))
        )
    except (TimeoutException, NoSuchElementException):
        assert False
    context.batch_home_page.associate_name().click()
    sleep(.5)
    assert context.batch_home_page.notes_box().get_attribute('value') == note_to_add
    context.batch_home_page.close_note().click()
