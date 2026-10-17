# define a tuple with paratenses
# tuple values are immutable, can not be changed

my_tuple = (1, "strings", True)
print(my_tuple[1])

print(type(my_tuple))

# you can define a tuple without parenteses - not a best practice
my_tuple2 = 1, "strings", 4.5, True

# check the number os ocurrences in a tuple
print(my_tuple.count("strings"))

# check the index of a element in a tuple
print(my_tuple2.index(4.5))

# print tuple
for x in my_tuple2:
    print(x)

# my_tuple[0] = 5  'tuple' object does not support item assignment