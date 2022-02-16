"""Order data, DTO"""
class Order:
	def __init__(self, id):
		self._id = id
		    

"""Processing of order-related operations"""
class OrderProcessor:

	def prepare_order(self, order) :
		print("Preparing order for: " + order._id)

	def pay_order(self, order) :
		print("Paying order for: " + order._id)

	def validate_order(self, order) :
		print("Validating order for: " + order._id)

	def finalize_order(self, order) :
		print("Finalizing order for: " + order._id)

	def ship_order(self, order) :
		print("Shipping order for: " + order._id)

