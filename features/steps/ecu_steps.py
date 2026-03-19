from behave import given, when, then
from ecu_validator import validate_speed

@given('ECU speed is 80')
def step_given_speed(context):
    context.speed = 80

@when('I validate the speed')
def step_validate(context):
    context.result = validate_speed(context.speed)

@then('the speed should be valid')
def step_result(context):
    assert context.result == True
