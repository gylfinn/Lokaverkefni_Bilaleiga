from Vehicle import Vehicle

class Hatchback(Vehicle):
    def __init__(self, registration_num, model_year, brand, price):
        super().__init__(registration_num, model_year, brand, price)