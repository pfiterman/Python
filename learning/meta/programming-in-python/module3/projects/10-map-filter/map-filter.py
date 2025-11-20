menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee

# maps take all objects in a list and applies a function
map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)

# filters do the same, but take the result and creates a new list with only the true values
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)