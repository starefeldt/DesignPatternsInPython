from pip._vendor import requests
import json

class OrderService:
	
	def check_availability(self, item_id):
		repository = OrderLocalInventoryRepository()
		return repository.in_stock(item_id)


class OrderLocalInventoryRepository:

	items = {
		'ItemID_1' : {'Name': 'PC', 'Brand': 'Microsoft'},
		'ItemID_2' : {'Name': 'PC', 'Brand': 'Apple'},
	}

	def in_stock(self, item_id):
		return item_id in self.items.keys()



####################### Dependency Injection ###############################

class OrderService_With_DI:

	def __init__(self, repository):
		self.repository = repository

	def check_availability(self, item_id):
		return self.repository.in_stock(item_id)


class OrderWarehouseInventoryRepository:

	def __init__(self, repository):
		self._repository = repository
	
	def in_stock(self, item_id):
		try:
			response = requests.get("https://demo_order_warehouse.se/" + item_id)
			json_response = response.json()
			response_dict = json.loads(json_response)
			available = response_dict['Available']
			if not available:
				#check if item is present at supplied repository
				available = self._repository.in_stock(item_id)
			return available
		except:
			#check if item is present at supplied repository
			return self._repository.in_stock(item_id)
