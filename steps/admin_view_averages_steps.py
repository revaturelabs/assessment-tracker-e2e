from behave import when, then


@when(u'The admin clicks the Assessments button')
def step_impl(context):
    context.admin_page.view_averages_button().click()


@then(u'The admin should be navigated to a page displaying averages of all assessments across Revature')
def step_impl(context):
    assert context.driver.title == "Assessment Tracker - Admin Assessment Dashboard"
    assert context.admin_average_page.DevOpsStackTable() is not None
    assert context.admin_average_page.JavaStackTable() is not None
    assert context.admin_average_page.AWSStackTable() is not None
    assert context.admin_average_page.averagesFromDevOpsStackTable() is not None
    assert context.admin_average_page.averagesFromJavaStackTable() is not None
    assert context.admin_average_page.averagesFromAWSStackTable() is not None
