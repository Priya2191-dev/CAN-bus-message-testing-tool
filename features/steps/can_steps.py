from behave import given, when, then
import time
from can_simulator import get_bus, create_message, send_message, receive_message

@given('a virtual CAN bus')
def given_bus(context):
    # Separate TX and RX buses
    context.bus_tx = get_bus()
    context.bus_rx = get_bus()

@when('I send a CAN message with ID {arb_id} and data {data}')
def when_send(context, arb_id, data):
    arb_id_int = int(arb_id, 16)
    data_list = [int(x) for x in data.split(",")]

    context.msg = create_message(arbitration_id=arb_id_int, data=data_list)

    status = send_message(context.bus_tx, context.msg)
    assert status is True

    # Polling instead of sleep
    start = time.time()
    context.received = None

    while time.time() - start < 2:
        context.received = receive_message(context.bus_rx, timeout=0.2)
        if context.received:
            break

@when('I do not send any CAN message')
def when_no_send(context):
    context.received = receive_message(context.bus_rx, timeout=1)

@then('I should receive the same CAN message')
def then_validate_same(context):
    try:
        assert context.received is not None, "No CAN message received"

        assert context.received.arbitration_id == context.msg.arbitration_id
        assert list(context.received.data) == list(context.msg.data)

    finally:
        # ALWAYS shutdown (even if assert fails)
        context.bus_tx.shutdown()
        context.bus_rx.shutdown()

@then('the received CAN message should match ID {arb_id} and data {data}')
def then_validate_specific(context, arb_id, data):
    try:
        arb_id_int = int(arb_id, 16)
        data_list = [int(x) for x in data.split(",")]

        assert context.received is not None, "No CAN message received"
        assert context.received.arbitration_id == arb_id_int
        assert list(context.received.data) == data_list

    finally:
        context.bus_tx.shutdown()
        context.bus_rx.shutdown()

@then('no CAN message should be received')
def then_validate_none(context):
    try:
        assert context.received is None
    finally:
        context.bus_tx.shutdown()
        context.bus_rx.shutdown()
