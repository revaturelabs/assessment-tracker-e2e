from behave import given, when, then


# @given('The Instructor is on a page for a {batch}')
# def step_impl(context, batch: str):
#     pass


@when(u'The Instructor clicks on an Associate {name} from a list')
def step_impl(context, name: str):
    pass


@when(u'The Instructor sets a grade for an {assessment}')
def step_impl(context, assessment: str):
    pass


@when(u'The Instructor clicks the button to save the Score')
def step_impl(context):
    pass


@then(u'A message should tell the Instructor that their grade was saved')
def step_impl(context):
    pass
