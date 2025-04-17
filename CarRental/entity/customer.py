class Customer:
    def __init__(self, firstName, lastName, email, phoneNumber, customerID=None):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__customerID = customerID

    def __str__(self):
        return f"Customer(firstName='{self.get_firstName()}', lastName='{self.get_lastName()}', email='{self.get_email()}', phoneNumber='{self.get_phone()}', customerID={self.get_customerID()})"

    def get_customerID(self): return self.__customerID
    def set_customerID(self, customerID): self.__customerID = customerID

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_phone(self): return self.__phoneNumber
    def set_phone(self, phoneNumber): self.__phoneNumber = phoneNumber
