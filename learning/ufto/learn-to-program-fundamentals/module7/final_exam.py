# 1 Evaluates to a float
print(7 + 8.5)
print(3 / 4)

# 2 
a = 7
b = a + 3
a = 9
print(b)

# 3
def f(y):
    x = y * 3
    return y + x

print(f(10)) # 40

# 4 Evaluates "pwn3d"
first = 'pwn'
second = 3
third = 'd'

print(first + str(second) + third)

# 5
def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.  Count how manytimes letter appears in s1 and in s2, and return the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))

print(count_max_letters('hello', 'world', 'l'))
print(count_max_letters('cat', 'abracadabra', 'a'))

# 6
def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the letters in prefix.
    '''
    return s1.startswith(prefix) and s2.startswith(prefix)

# 7
def moogah(a, b):
    '''(str, int) -> str'''

def frooble(L):
    '''(list of str) -> int
    Precondition: L has at least one element.'''

# moogah("a", frooble(["a"]))
# lst = ["a", "b", "c"]
# moogah(lst[0], len(lst))

# 8
def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + 2

    return result

print(gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2))

# 9
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:
        if k in d:
            result.append(k)

    return result

print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))

# 10
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d:
             result = result + 1

    return result

print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
print(count_values_that_are_keys({1: 1}))
print(count_values_that_are_keys({1: 2, 2: 3, 3: 0}))
print(count_values_that_are_keys({1: 2}))

# 11
def double_values(collection):
    for v in range(len(collection)):
         collection[v] = collection[v] * 2

L = [1, 2, 3]
double_values(L)

d = {0: 10, 1: 20, 2: 30}
double_values(d)

# 12
# (1)  3   5   
#  2  (4)  5  
#  4   0  (8)

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            # if row == col:
            #     diagonal.append(L[row][col])
            # else:
            #     non_diagonal.append(L[row][col])
            
            # if row == col:
            #     diagonal.append(L[row][col])
            # if row != col:
            #     non_diagonal.append(L[row][col])

            # if row == col:
            #     diagonal.append(L[row][col])
            # elif row != col:
            #     non_diagonal.append(L[row][col])

            if row == col:
                diagonal.append(L[row][row])
            else:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)

print(get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]]))

# 13
def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] = d[c] + 1

letter_counts = {'i': 0, 'r': 5, 'e': 1}
add_to_letter_counts(letter_counts, 'eerie')
print(letter_counts)