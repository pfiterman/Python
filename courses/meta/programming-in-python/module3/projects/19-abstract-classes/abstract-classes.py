# abstract classes

# - Can't create an instance
# - Python does not support absatraction directly
# - Methods must be defined before they can be implemented

# abstract classes lack implementation on their own
# methods must be implemented in the derived classes

from abc import ABC, abstractmethod # decorator

class SomeAbstractClass(ABC):
    @abstractmethod
    def someabstractmethod(self):
        pass

# A decorator is a function that takes another function as its arguments and gives a new function as an output

# Any given abastrct class can consist of one or more abstract methods
# However a  class that has an abstract class as its parent can not be instantiate unless you override all the abastract methods


class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")

amounts = []
john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)