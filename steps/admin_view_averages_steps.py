from behave import when, then


@when(u'The admin clicks the Assessments button')
def step_impl(context):
    context.admin_page.view_averages_button().click()


@then(u'The admin should be navigated to a page displaying averages of all assessments across Revature')
def step_impl(context):
    assert context.driver.title == "Assessment Tracker - Admin Assessment Dashboard"
    assert context.admin_average_page.get_tables() is not None
    assert context.admin_average_page.get_table_averages() is not None
