from order_inventory_classes import *

def order(item_id):
    service = OrderService()
    available = service.check_availability(item_id)
    print("{0} |{1} | {2} | In stock: {3}".format(type(service).__name__, None , item_id, available))
    # more steps...

print("---------------------------------------------------------------------")
order("ItemID_1")
order("ItemID_2")
order("ItemID_3")
print("---------------------------------------------------------------------")


####################### Dependency Injection ###############################

def order_better(item_id, repository):
    service = OrderService_Better(repository)
    available = service.check_availability(item_id)
    print("{0} |{1} | {2} | In stock: {3}".format(type(service).__name__, type(repository).__name__ , item_id, available))
    # more steps...

order_better(
    "ItemID_1", 
    OrderLocalInventoryRepository())

order_better(
    "ItemID_2", 
    OrderWarehouseInventoryRepository(
        OrderLocalInventoryRepository()))

order_better(
    "ItemID_3", 
    OrderWarehouseInventoryRepository(
        OrderLocalInventoryRepository()))

print("---------------------------------------------------------------------")