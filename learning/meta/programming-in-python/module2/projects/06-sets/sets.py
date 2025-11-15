# set don't allow duplicate values
set_a = {1, 2, 3, 4, 5}
print(set_a)

set_a = {1, 2, 3, 4, 5, 5}
print(set_a) # seconf five is not inserted

set_a.add(6)
set_a.remove(2)
set_a.discard(3)
print(set_a)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)

print(set_a.difference(set_b))
print(set_a - set_b)

# elements present in set_a or setb_b but not in both sets
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)