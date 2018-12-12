
class CustomerOrderHistory:
    def __init__(self, manager):
        self.__manager = manager 

    def getOrderHistory(self):
        customer = self.__manager.getMetadata()
        order_history = self.__manager.getOrderManager().getOrdersByCustomer(customer.getSSN())
        for order in order_history:
            print(order)

