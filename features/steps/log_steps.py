from behave import given, when, then
from log_replay import replay


@given('a valid CAN log')
def given_valid_log(context):
    context.log = [{"id": 0x101, "data": [1, 2]}]
    context.error = None

@given('multiple CAN frames')
def given_multiple(context):
    context.log = [
        {"id": 0x101, "data": [1, 2]},
        {"id": 0x102, "data": [3, 4]},
    ]
    context.error = None


@given('an invalid CAN log')
def given_invalid(context):
    context.log = "invalid"
    context.error = None


@when('I replay the log')
def when_replay(context):
    try:
        replay(context.log)
    except Exception as e:
        context.error = e


@then('CAN messages should be printed')
def then_output(context):
    assert context.error is None


@then('all messages should be printed')
def then_all_output(context):
    assert context.error is None


@then('replay should fail')
def then_fail(context):
    assert context.error is not None
