# a = 5 / 0
# print(a) #ZeroVivisionError: division by zero

def divide_by(a, b):
    return a / b

try:
    ans = print(divide_by(40, 0))
except ZeroDivisionError as e:    
    print(e, "we cannot divide by zero")
    print(e.__class__)
except Exception as e:
    print(e, "something went wrong")

