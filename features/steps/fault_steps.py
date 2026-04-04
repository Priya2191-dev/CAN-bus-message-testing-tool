from behave import given, when, then
from fault_injection import inject_fault


@given('normal CAN data')
def given_data(context):
    context.data = [10, 20, 30]
    context.result = None
    context.error = None

@when('I inject a fault')
def when_default_fault(context):
    try:
        context.result = inject_fault(context.data)
    except Exception as e:
        context.error = e

@when('I inject a fault at index {index}')
def when_fault_index(context, index):
    try:
        context.result = inject_fault(context.data, index=int(index))
    except Exception as e:
        context.error = e

@when('I inject a fault with value {value}')
def when_fault_value(context, value):
    try:
        context.result = inject_fault(context.data, fault_value=int(value))
    except Exception as e:
        context.error = e

@then('data should be corrupted at index {index}')
def then_validate_index(context, index):
    idx = int(index)

    assert context.error is None, f"Unexpected error: {context.error}"
    assert context.result[idx] == 255

@then('fault injection should fail')
def then_validate_failure(context):
    assert context.error is not None
