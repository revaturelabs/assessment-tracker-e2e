from behave import given, when, then
from selenium.common.exceptions import ElementNotInteractableException



# @given('The Instructor is on a page for a specific {batch}')
# def step_impl(context, batch: str):
#     if batch == "Python - 20200120":
#         context.home_page.batch_button_1().click()
#     elif batch == "iOS Development - 20210320":
#         context.home_page.batch_button_2().click()
#     elif batch == "C++ - 20202222":
#         context.home_page.batch_button_3().click()


@when(u'The Instructor clicks on an Associate {name} from a list')
def step_impl(context, name: str):
    if name == "Zachary":
        context.driver.implicitly_wait(3)
        context.batch_home_page.get_name_1().click()
    elif name == "Kerry":
        context.driver.implicitly_wait(3)
        context.batch_home_page.get_name_2().click()
    elif name == "Patrick":
        context.driver.implicitly_wait(3)
        context.batch_home_page.get_name_3().click()


@when(u'The Instructor sets a grade for an {assessment}')
def step_impl(context, assessment: str):
    if assessment == "TEST":
        context.driver.implicitly_wait(3)
        context.batch_home_page.set_grade_1().clear()
        context.batch_home_page.set_grade_1().send_keys("100")
    elif assessment == "iOS Quiz":
        context.driver.implicitly_wait(3)
        context.batch_home_page.set_grade_2().clear()
        context.batch_home_page.set_grade_2().send_keys("70")
    elif assessment == "Cumulative":
        context.driver.implicitly_wait(3)
        context.batch_home_page.set_grade_3().clear()
        context.batch_home_page.set_grade_3().send_keys("20")


@when(u'The Instructor clicks the {button} to save the Score')
def step_impl(context, button):
    if button == "save1":
        context.batch_home_page.save_button_1().click()
    elif button == "save2":
        context.batch_home_page.save_button_2().click()
    elif button == "save3":
        context.batch_home_page.save_button_3().click()


@then(u'A message should tell the Instructor that their grade was saved')
def step_impl(context):
    context.driver.get("http://34.204.173.118:5000/home")
