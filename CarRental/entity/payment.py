import pyodbc
class Payment:
    def __init__(self, paymentID=None, leaseID=None, paymentDate=None, amount=None):
        self.paymentID = paymentID
        self.leaseID = leaseID
        self.paymentDate = paymentDate
        self.amount = amount

    def __str__(self):
        return f"Payment(paymentID={self.paymentID}, leaseID={self.leaseID}, paymentDate='{self.paymentDate}', amount={self.amount})"

    def get_paymentID(self): return self.__paymentID
    def set_paymentID(self, paymentID): self.__paymentID = paymentID

    def get_leaseID(self): return self.__leaseID
    def set_leaseID(self, leaseID): self.__leaseID = leaseID

    def get_paymentDate(self): return self.__paymentDate
    def set_paymentDate(self, paymentDate): self.__paymentDate = paymentDate

    def get_amount(self): return self.__amount
    def set_amount(self, amount): self.__amount = amount