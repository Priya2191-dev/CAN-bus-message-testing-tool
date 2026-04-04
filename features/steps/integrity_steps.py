from behave import given, when, then
from integrity import checksum, verify


@given('valid CAN data')
def step_valid_data(context):
    context.data = [10, 20, 30]
    context.expected_checksum = checksum(context.data)
    context.result = None

@given('CAN data [255, 1]')
def step_overflow_data(context):
    context.data = [255, 1]
    context.expected_checksum = checksum(context.data)

@when('I calculate checksum')
def step_calculate(context):
    context.calculated = checksum(context.data)
    context.result = verify(context.data, context.expected_checksum)

@when('I modify CAN data')
def step_modify(context):
    context.data[0] = 99  # simulate corruption
    context.result = verify(context.data, context.expected_checksum)

@then('integrity should be verified')
def step_verified(context):
    assert context.result is True

@then('integrity verification should fail')
def step_failed(context):
    assert context.result is False
