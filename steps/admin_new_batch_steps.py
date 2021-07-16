from time import sleep
from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'The User enters a batch name in the batch name input')
def step_impl(context):
    context.admin_page.batch_name_input().send_keys("Selenium Automation Test Batch")


@when(u'The User enters a track name in the track name input')
def step_impl(context):
    context.admin_page.training_track_input().send_keys("AutomationTestTrack")


@when(u'The User enters an end date in the end date input')
def step_impl(context):
    context.admin_page.end_date_input().send_keys("12/31/2021")


@when(u'The User selects a trainer')
def step_impl(context):
    context.admin_page.trainer_input().select_by_visible_text("Mark Mambo")

@when(u'The User selects a co-trainer')
def step_impl(context):
    context.admin_page.co_trainer_input().select_by_visible_text("Bill Gates")


@when(u'The User selects five associates to be added to the new batch')
def step_impl(context):
    interested_associates = context.admin_page.unadded_associates()[:5]
    for associate in interested_associates:
	    associate.find_element_by_class_name("associateCheck").click()


@then(u'The five selected associates should appear in the added associates list')
def step_impl(context):
    assert len(context.admin_page.added_associates()) == 5


@when(u'The submit create new batch button is pressed')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    context.admin_page.submit_batch_button().click()


@then(u'A batch created popup should appear')
def step_impl(context):
	try:
		WebDriverWait(context.driver, 5).until(EC.alert_is_present())
		alert = context.driver.switch_to.alert
		alert.accept()
		assert True
	except TimeoutException:
		assert False


@when(u'The User enters ba into the search input')
def step_impl(context):
    WebDriverWait(context.driver, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "associateList")))
    context.admin_page.search_associate_input().send_keys("ba")


@then(u'All associates in the associate list should start with ba')
def step_impl(context):
    all_associates = context.admin_page.unadded_associates()
    for associate in all_associates:
        if not associate.value_of_css_property("display") == "none":
            assert associate.text.lower()[:2] == 'ba'


@when(u'The User selects the associates in the associate list')
def step_impl(context):
    for associate in context.admin_page.unadded_associates():
        if not associate.value_of_css_property("display") == "none":
            associate.find_element_by_class_name("associateCheck").click()


@then(u'The selected associates should appear in the added associates list')
def step_impl(context):
    for associate in context.admin_page.added_associates():
        assert associate.text.lower()[:2] == 'ba'