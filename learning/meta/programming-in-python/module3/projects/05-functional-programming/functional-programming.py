# Tradional Functions

# 1. Access global state
# 2. Modify global variables
# 3. Access local state
# 4. Change args
# 5. Output does not depends on Input

# Pure Functions

# 1. Do not access global state
# 2. Do not modify global variables
# 3. Access local state
# 4. Do not change args
# 5. Output depends on Input

# In Python, functions are what's know as first-class citizen
# They have the same level of strings and numbers
# They can be:
# 1. Assigned to a variable
# 2. Passed as an argument
# 3. Returned to its caller

coffees = ["Expresso", "Latte", "Cappuccino", "Macchiato", "Americano", "Decaf"]
print(sorted(coffees))

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)