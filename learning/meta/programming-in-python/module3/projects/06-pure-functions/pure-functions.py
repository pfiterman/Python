# Pure functions
# Does not change or have any effect on a variable, data, list or set in a global scope

# Pure function or not?
global_list = [1, 2, 3]

def add_to(item):
    return global_list.append(item)

add_to(4)
print(global_list)

# It's not a pure function because it's changing the global_list variable in the global scope

# To become a pure function it must:
# 1. accept list as argument
# 2. add items to the list without modifying the original one
# 3. return a new list with the new item

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

# Benefits of pure functions:
# 1. know the outcome
# 2. consistent and reliable
# 3. cache
# 4. multi=threaded programs

