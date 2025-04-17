class Car:
    def __init__(self, vehicleID, make, model, year, dailyRate, status, passengerCapacity, engineCapacity):
        self.__vehicleID = vehicleID  # Keep vehicleID as an integer
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity

    # Getter for vehicleID
    def get_vehicleID(self):
        return self.__vehicleID

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_dailyRate(self):
        return self.__dailyRate

    def get_status(self):
        return self.__status

    def get_passengerCapacity(self):
        return self.__passengerCapacity

    def get_engineCapacity(self):
        return self.__engineCapacity

    def __str__(self):
        return f"Car(vehicleID={self.__vehicleID}, make={self.__make}, model={self.__model}, year={self.__year}, dailyRate={self.__dailyRate}, status={self.__status}, passengerCapacity={self.__passengerCapacity}, engineCapacity={self.__engineCapacity})"
