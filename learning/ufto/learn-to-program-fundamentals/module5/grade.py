# 1
exp1 = len([1, 2, 3]) == len(['a', 'b', 'c'])
exp2 = int('3') in [len('a'), len('ab'), len('abc')]
exp3 = len('mom') in [1,2,3]

print(exp1)
print(exp2)
print(exp3)

# 2
def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result

# mystery('abc')

# 3
def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

# Return a list containing every third item from L starting at index 0

# 4
def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements  from L concatenated together, starting with indices 0 and 1, 2 and 3, and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i + 2
    return compressed_list

print(compress_list(['a', 'b', 'c', 'd']))

# 5
sum_even = 0
num = 524
while num <= 10508:
    sum_even = sum_even + num
    num = num + 2
    
print(sum_even)

sum_even = 0
for num in range(524, 10508 + 1, 2):
    sum_even = sum_even + num

print(sum_even)

# 27541388

# 6
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

print(while_version([1, 2, 3, 4, 5, 6]))

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

print(for_version([1, 2, 3, 4, 5, 6]))

# 7
numbers = [1, 4, 3]
numbers.reverse()
print(numbers)

#8
fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)


#9
playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let it Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola', 'Lola']

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    # while playlist.count(song) >= 3:
    #     playlist.remove(song)
    
    # while playlist.count(song) > 3:
    #     playlist.pop(playlist.index(song))

    # while playlist.count(song) > 3:
    #     playlist.remove(song)
    
cap_song_repetition(playlist, 'Lola')
print(playlist)

#10 all of them
a = [1, 2, 3]
b = a
# MISSING CODE HERE
# a[1] = 'A'
# b[1] = 'AB'
# a[1] = a[1][0]
# b[-2] = 'A'
a = [1, 'A', 3]
b = [1, 'A', 3]
print('Question 10')
print(a, b)
# [1, 'A', 3] [1, 'A', 3]

# 11 
a = [1, 2, 3]
b = [1, 2, 3]
# MISSING CODE HERE
print('Question 11')
a = [1, 'A', 3]
b = [1, 'A', 3]
print(a, b)
# [1, 'A', 3] [1, 'A', 3]

# 12
def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

print('Question 12')
values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

# 13 print [3, 6, 9]
print('Question 13')
values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)

#14 produces 3 11 19
print('Question 14')
# range(3, 23, 8)
# range(3, 20, 8)
for num in range(3, 20, 8):
    print(num)