# 1
d = {'a': 1, 'b': 2}
# CODE MISSING HERE
d["c"] = 3
d # {'a': 1, 'c': 3, 'b': 2}
print(d)

# 2
d = {'a': 1, 'b': 2}
# CODE MISSING HERE
d["b"] = 3
d # {'a': 1, 'b': 3}
print(d)

# 3
d = {'a': [1, 3], 'b': [5, 7]}
# CODE MISSING HERE

# d["a"].append(2)
# d["a"].sort()

d["a"].insert(1,2)

d # {'a': [1, 2, 3], 'b': [5, 7]}
print(d)

# 4 evaluates True
d = {'a': 1, 'c': 3, 'b': 2}
# "b" in d
# not ("e" in d)

# 5 Evaluate 3
d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}
# print(len(d["b"]))
# print(len(d))

# 6 Result in an error
tup = (1, 2, 3)
# tup.reverse()
# tup[-2] = 4

# 7
# ("single",)
# (1, "fred0", 2.0)

# 8
d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}

# total = 0
# for k in d:
#     total = total + len(d[k])

L = []
for k in d:
    L.extend(d[k])

total = len(L)

print(total)

# 9 Shell evaluates
{1: 10, 1: 20, 1: 30}
# {1: 30}

# 10
L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]

# Populates dictionary d where each key is the first item of each inner list L and eah value is the second item of thet inner list

# 11
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

# Try to eat one of each fruit: reduce by 1 all quantities greater than 0 associated wit each fruit in d and retur True if and only if any fruit was eaten

# 12
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in  d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE
    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True

    return found

print(contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}))
print(contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))