class Lease:
    def __init__(self, leaseID=None, customerID=None, vehicleID=None, startDate=None, endDate=None, type=None, returned=False):
        self.__leaseID = leaseID
        self.__customerID = customerID
        self.__vehicleID = vehicleID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__type = type
        self.__returned = returned

    # Getter methods for private attributes
    @property
    def leaseID(self):
        return self.__leaseID

    @property
    def customerID(self):
        return self.__customerID

    @property
    def vehicleID(self):
        return self.__vehicleID

    @property
    def startDate(self):
        return self.__startDate

    @property
    def endDate(self):
        return self.__endDate

    @property
    def type(self):
        return self.__type

    @property
    def returned(self):
        return self.__returned

    def __str__(self):
        return f"Lease(leaseID={self.leaseID}, customerID={self.customerID}, vehicleID={self.vehicleID}, " \
               f"startDate='{self.startDate}', endDate='{self.endDate}', type='{self.type}', returned='{self.returned}')"
