import math
import cProfile
import binary_search, linear_search

L = ["a", "b", "c", "a", "d"]
print(L.index("a")) # 0
print(L.index("c")) # 2
print(L.index("d")) # 4

print(math.log(2, 2)) # 1.0
print(math.log(4, 2)) # 2.0
print(math.log(8, 2)) # 3.0
print(math.log(16, 2)) # 4.0
print(math.log(32, 2)) # 5.0

print(math.log(1000000000,2)) # 29.89

L = list(range(10000000))
print(binary_search.binary_search(L, 10000000))
print(linear_search.linear_search(L, 10000000))

cProfile.run("binary_search.binary_search(L, 10000000)")
cProfile.run("linear_search.linear_search(L, 10000000)")