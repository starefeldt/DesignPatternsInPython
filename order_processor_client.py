from order_processor_classes import *

def process_order_payment(order):
    processor = OrderProcessor()
    processor.prepare_order(order)
    processor.pay_order(order)

def process_order_shipment(order):
    processor = OrderProcessor()
    processor.validate_order(order)
    processor.finalize_order(order)
    processor.ship_order(order)

process_order_payment(Order("OrderID_1"))
print()

process_order_shipment(Order("OrderID_2"))
print()