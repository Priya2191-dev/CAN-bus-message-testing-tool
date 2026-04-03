from behave import given, when, then
import can
import time
from can_simulator import get_bus, create_message, send_message, receive_message


@given('a virtual CAN bus')
def step_bus(context):
    context.bus = get_bus()

@when('I send a CAN message with ID {arb_id} and data {data}')
def step_send(context, arb_id, data):
    arb_id_int = int(arb_id, 16)
    data_list = [int(x) for x in data.split(",")]

    context.msg = create_message(arbitration_id=arb_id_int, data=data_list)
    context.send_status = send_message(context.bus, context.msg)

    # Better than sleep → small polling wait
    start = time.time()
    while time.time() - start < 2:
        context.received = receive_message(context.bus, timeout=0.2)
        if context.received:
            break

@when('I do not send any CAN message')
def step_no_send(context):
    context.received = receive_message(context.bus, timeout=1)

@then('I should receive the same CAN message')
def step_validate_same(context):
    assert context.send_status is True
    assert context.received is not None, "No CAN message received"

    assert context.received.arbitration_id == context.msg.arbitration_id
    assert list(context.received.data) == list(context.msg.data)

    context.bus.shutdown()

@then('the received CAN message should match ID {arb_id} and data {data}')
def step_validate_specific(context, arb_id, data):
    arb_id_int = int(arb_id, 16)
    data_list = [int(x) for x in data.split(",")]

    assert context.received is not None
    assert context.received.arbitration_id == arb_id_int
    assert list(context.received.data) == data_list

    context.bus.shutdown()

@then('no CAN message should be received')
def step_validate_none(context):
    assert context.received is None
    context.bus.shutdown()
