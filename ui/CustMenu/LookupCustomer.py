class LookUpCustomer:
    def __init__(self, manager):
        self.__manager = manager

    def lookupCustomer(self):
        self.__manager.gotoClass("lookupcustomermenu")