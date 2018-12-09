class LookUpCustomer:
    def __init__(self, manager):
        self.__manager = manager

    def lookUpCustomer(self):
        self.__manager.gotoClass("lookupcustomermenu")