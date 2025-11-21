class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take the leave for " + str(days) + " days"
    
adrian = Employees("Adrian", "A")
jhon = Supervisors("Jhon", "J", "Doe")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(jhon.password)
print(emily.name)