from behave import when, then


@when('The User clicks on a batch {batch}')
def step_impl(context, batch: str):
    if batch == "temp":
        context.home_page.python_batch_button().click()
    elif batch == "temp2":
        context.home_page.java_batch_button().click()


@then('The title should say {title}')
def step_impl(context, title: str):
    assert context.driver.title == title
