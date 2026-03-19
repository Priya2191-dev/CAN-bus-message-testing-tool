from behave import given, when, then
import can

@given('a virtual CAN bus')
def step_bus(context):
    context.bus = can.Bus(interface='virtual', channel='test')

@when('I send a CAN message')
def step_send(context):
    context.msg = can.Message(arbitration_id=0x123, data=[1,2,3,4])
    context.bus.send(context.msg)

@then('I should receive the same CAN message')
def step_receive(context):
    received = context.bus.recv(timeout=1)
    assert received is not None
    assert received.arbitration_id == context.msg.arbitration_id
    context.bus.shutdown()
