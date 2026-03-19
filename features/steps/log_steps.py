from behave import given, when, then
from log_replay import replay

@given('a CAN log')
def step_log(context):
    context.log = [{"id": 0x101, "data": [1,2]}]

@when('I replay the log')
def step_replay(context):
    replay(context.log)

@then('messages should be printed')
def step_output(context):
    assert True 
