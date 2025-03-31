# Lists can be written as a list of comma-separated values (items) between square brackets
squares = [1, 4, 9, 16, 25]
print(f"squares={squares}")

# Lists can be indexed and slices like strings
print(f"squares[0]={squares[0]}")
print(f"squares[-1]={squares[-1]}")
print(f"squares[-3:]={squares[-3:]}")

# All slice operations return a new list containing the requested elements
print(f"squares[:]={squares[:]}")

# Lists also support operations like concatenation
squares2 = squares + [36, 49, 64, 81, 100]
print(f"squares2 = squares + [36, 49, 64, 81, 100] = {squares2}")

# Lists are a mutable type, i.e. it is possible to change their content
cubes = [1, 8, 27, 65, 125] #something wrong here, the cube of 4 (4 ** 3) is 64, not 65!
cubes[3] = 64
print(f"cubes = {cubes}")

# You can also add new items at the end of the list, by using the append() method
cubes.append(216) #add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(f"cubes = {cubes}")

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"letters = {letters}")

letters[2:5] = ['C', 'D', 'E'] #replacing some values
print(f"letters = {letters}")

letters[2:5] = [] #removing values
print(f"letters = {letters}")

letters[:] = [] # clear the list by replacing all the elements with an empty list
print(f"letters = {letters}")

# The built-in function len() also applies to lists
letters = ['a', 'b', 'c', 'd']
print(f"len(letters) = {len(letters)}")

# It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2 ,3]
x = [a, n]
print(f"x = {x}")
print(f"x[0] = {x[0]}")
print(f"x[0][1] = {x[0][1]}")
