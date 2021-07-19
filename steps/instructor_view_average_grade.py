from behave import then


@then(u'The average grade is displayed on the batch page')
def step_impl(context):
    try:
        average: str = context.batch_home_page.assessment_average().text
        float(average)
    except ValueError:
        assert False
