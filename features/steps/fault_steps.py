from behave import given, when, then
from fault_injection import inject_fault

@given('normal CAN data')
def step_data(context):
    context.data = [10, 20, 30]

@when('I inject a fault')
def step_fault(context):
    context.result = inject_fault(context.data.copy())

@then('data should be corrupted')
def step_verify(context):
    assert context.result[0] == 255
