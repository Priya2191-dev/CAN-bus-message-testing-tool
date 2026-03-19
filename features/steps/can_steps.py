from behave import given, when, then
import can
import time

@given('a virtual CAN bus')
def step_bus(context):
    # Use SAME channel for TX and RX
    context.bus_tx = can.Bus(interface='virtual', channel='test')
    context.bus_rx = can.Bus(interface='virtual', channel='test')

@when('I send a CAN message')
def step_send(context):
    context.msg = can.Message(arbitration_id=0x123, data=[1,2,3,4])
    context.bus_tx.send(context.msg)

    # IMPORTANT: allow time for message propagation
    time.sleep(0.1)

@then('I should receive the same CAN message')
def step_receive(context):
    received = context.bus_rx.recv(timeout=2)

    assert received is not None, "No CAN message received"
    assert received.arbitration_id == context.msg.arbitration_id

    # Proper shutdown (fix warning)
    context.bus_tx.shutdown()
    context.bus_rx.shutdown()
