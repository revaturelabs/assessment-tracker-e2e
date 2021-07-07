from behave import given, when, then


@given(u'The User is logged in as an Instructor')
def step_impl(context):
    context.driver.get("http://34.204.173.118:5000/home")
    context.home_page.login_button().click()


@given(u'The Instructor is on a page for a Batch')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The Instructor is on a page for a Batch')


@when(u'The Instructor clicks on a Plus Assessment Button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor clicks on a Plus Assessment Button')


@when(u'The Instructor selects an Assessment Type')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor selects an Assessment Type')


@when(u'The Instructor enters a name for the Assessment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor enters a name for the Assessment')


@when(u'The Instructor clicks the button to create the Assessment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor clicks the button to create the Assessment')


@then(u'The list of Assessments for that week is updated with the new one')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The list of Assessments for that week is updated with the new one')
