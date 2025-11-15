# local scope
# Local scope refers to a variable that are declared inside a function

def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2)) # 7


# Accessing variable outside of the function:
print(total) # NameError: name 'total' is not defined