from behave import given, when, then
from integrity import checksum, verify

@given('CAN data [10, 20, 30]')
def step_data(context):
    context.data = [10, 20, 30]

@when('I calculate checksum')
def step_checksum(context):
    context.cs = checksum(context.data)

@then('integrity should be verified')
def step_verify(context):
    assert verify(context.data) == True
