class Validator:
    def __init__(self):
        pass

    def ValidateSSN(self, SSN):
        valid = True
        
        #try to cast to INT.
        try:
            int(SSN)
        except:
            valid = False
            return valid

        #Check length == 10
        if len(SSN) == 10:
            pass
        else:
            valid = False
            return valid
        
        #Check date in range 01 - 31
        if not 0 <  int(SSN[:2]) <= 31:
            valid = False
            return valid

        #Check month in range 1-12
        if not 0 <  int(SSN[2:4]) <= 12:
            valid = False
            return valid

        return valid
    
    def ValidateOrderId(self, orderid):
        valid = True

        try:
            int(orderid)
        except:
            valid = False
            return valid
    
    def ValidateCarNumber(self, carnum):
        valid = True

        try:
            int(carnum)
        except:
            valid = False
            return valid

        #Check if first 2 are string
        #if int() cast fails then it is a string
        try:
            int(carnum[:2])
            valid = False
            return valid
        except:
            pass

        try:
            int(carnum[-2:])
        except:
            valid = False
            return valid

        return valid