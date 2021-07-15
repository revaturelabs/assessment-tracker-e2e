from behave import when, then


@when(u'The Instructor selects a week')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor selects a week')


@when(u'The Instructor clicks on an associate\'s name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The Instructor clicks on an associate\'s name')


@then(u'A popup appears where the Instructor can add or edit a note')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A popup appears where the Instructor can add or edit a note')


@then(u'The Instructor adds their note')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The Instructor adds their note')


@then(u'The Instructor clicks Submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The Instructor clicks Submit')


@then(u'The new note is saved')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The new note is saved')
