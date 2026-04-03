from behave import given, when, then
from ecu_validator import validate_speed


@given('ECU system is initialized')
def step_init(context):
    context.error = None
    context.result = None

@given('ECU speed is {speed}')
def step_given_speed(context, speed):
    try:
        # Handle numeric + string cases
        if speed.isdigit():
            context.speed = int(speed)
        else:
            context.speed = speed.strip('"')
    except Exception:
        context.speed = speed

@when('I validate the speed')
def step_validate(context):
    try:
        context.result = validate_speed(context.speed)
    except Exception as e:
        context.error = e

@then('the speed should be valid')
def step_valid(context):
    assert context.error is None, f"Unexpected error: {context.error}"
    assert context.result is True

@then('validation should fail')
def step_invalid(context):
    assert context.error is not None
