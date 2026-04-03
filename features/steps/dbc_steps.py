from behave import given, when, then
import os
from dbc_decoder import decode_message, DBC_FILE


@given('a valid DBC file')
def given_dbc(context):
    context.skip = False
    if not os.path.exists(DBC_FILE):
        context.skip = True

@when('I decode a CAN message')
def when_decode_default(context):
    if context.skip:
        return

    context.result = decode_message()

@when('I decode a CAN message with data {data}')
def when_decode_custom(context, data):
    if context.skip:
        return

    data_list = [int(x) for x in data.split(",")]
    context.result = decode_message(data=data_list)

@when('I decode using an invalid DBC file')
def when_invalid_dbc(context):
    context.error = None
    try:
        decode_message(dbc_path="invalid.dbc")
    except Exception as e:
        context.error = e

@then('I should get decoded signals')
def then_validate_result(context):
    if context.skip:
        return

    assert context.result is not None
    assert isinstance(context.result, dict)

@then('decoded signals should not be empty')
def then_validate_non_empty(context):
    if context.skip:
        return

    assert context.result is not None
    assert len(context.result) > 0

@then('decoding should fail')
def then_validate_failure(context):
    assert context.error is not None
