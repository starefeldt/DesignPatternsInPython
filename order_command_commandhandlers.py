from order_command_commands import *

# Order Payment Commands
class PrepareOrderCommandHandler:
	def execute(self, command : OrderPaymentCommand) :
		print("Preparing order for: " + command._id)

class PayOrderCommandHandler:
	def execute(self, command : OrderPaymentCommand) :
		print("Paying order for: " + command._id)

# Order Shipment Commands
class FinalizeOrderCommandHandler:
	def execute(self, command : OrderShipmentCommand) :
		print("Finalizing order for: " + command._id)

class ValidateOrderCommandHandler:
	def execute(self, command : OrderShipmentCommand) :
		print("Validating order for: " + command._id)

class ShipOrderCommandHandler:
	def execute(self, command : OrderShipmentCommand) :
		print("Shipping order for: " + command._id)

