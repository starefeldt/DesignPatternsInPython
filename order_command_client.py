from order_command_commands import *
from order_command_commandhandlers import *

def process_order(command, work_steps):
    for step in work_steps:
        step.execute(command)

process_order(OrderPaymentCommand("OrderID_1"), [
    PrepareOrderCommandHandler(),
    PayOrderCommandHandler()
])
print()

process_order(OrderShipmentCommand("OrderID_2"), [
    ValidateOrderCommandHandler(),
    FinalizeOrderCommandHandler(),
    ShipOrderCommandHandler()
])
print()