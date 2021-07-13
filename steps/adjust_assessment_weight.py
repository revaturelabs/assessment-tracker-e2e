from behave import when, then
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('The Instructor clicks on a quiz')
def instructor_selects_a_quiz(context):
    try:
        WebDriverWait(context.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[onclick*='.assessment']"))
        )
    except NoSuchElementException:
        assert False

    context.batch_home_page.week1_assessment_btn().click()


@then('The adjust-weight popup should be visible')
def the_test_weight_popup_isvisible(context):
    modal: WebElement = context.batch_home_page.adjust_weight_modal()
    assert modal.get_attribute("class").find("show")


@when('The Instructor moves the dial to {num}')
def moves_dial(context, num: int):
    slider: WebElement = context.batch_home_page.weight_slider()
    action: ActionChains = ActionChains(context.driver)
    action.click_and_hold(slider)
    action.drag_and_drop_by_offset(slider, -100, 0).release().perform()
    action.drag_and_drop_by_offset(slider, num, 0).release().perform()
    assert slider.get_attribute("value") == str(num)


@when('The Instructor clicks the save button')
def clicks_save_button(context):
    element: WebElement = context.batch_home_page.slider_submit_btn().click()


@then('The test-weight popup should disappear')
def test_save_popup_disappears(context):
    modal: WebElement = context.batch_home_page.adjust_weight_modal_hidden()
    print(modal.get_attribute("class"))
    assert modal.get_attribute("class").find("fade")


@then('The adjust-weight indicator should be {num}')
def test_weight_indicator_is(context, num: int):
    slider: WebElement = context.batch_home_page.weight_slider()
    assert slider.get_attribute("value") == "61"
