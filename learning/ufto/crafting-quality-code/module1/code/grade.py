# 1 
def is_palindrome_v3(s):
   """ (str) -> bool

   Return True if and only if s is a palindrome.
   
   >>> is_palindrome_v3('noon')
   True
   >>> is_palindrome_v3('racecar')
   True
   >>> is_palindrome_v3('dented')
   False
   """
   # j = len(s) - 1
   # for i in range(len(s) // 2):
   #    if s[i] != s[j - i]:
   #       return False
   # return True

   for i in range(len(s) // 2):
      if s[i] != s[len(s) - i - 1]:
           return False
   return True

print("Question 1")
print(is_palindrome_v3('noon'))
print(is_palindrome_v3('racecar'))
print(is_palindrome_v3('dented'))
print(is_palindrome_v3('a'))
print(is_palindrome_v3('ab'))
print(is_palindrome_v3('aa'))


# 2 
def is_anagram(s1, s2):
    """ (str, str) -> bool
   
    Return True if and only if s1 is an anagram of s2.
  
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """
    # d1 = {}
    # for char in s1:
    #     d1[char] = s1.count(char)
    # d2 = {}
    # for char in s2:
    #     d2[char] = s2.count(char)
    # return d1 == d2

    # l1 = list(s1)
    # l2 = list(s2)
    # l1.sort()
    # l2.sort()
    # return l1 == l2
    
print("Question 2")
print(is_anagram("silent", "listen"))
print(is_anagram("bear", "breach"))

# 3 Correct
def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.
  
    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """

    ch_strings = []

    for item in L:
        if item[0] == ch:
            ch_strings.append(item)

    return len(ch_strings)

# Use a list accumulator
# For each item in L, if the item begins with ch, add it to the accumulator
# Return the length of the accumulator

# 4 Correct
def count_startswith(L, ch):
   """ (list of str, str) -> int

   Precondition: the length of each item in L is >= 1, and len(ch) == 1

   Return the number of strings in L that begin with ch.

   >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
   2
   """
   # startswith = L[:]

   # for item in L:
   #    if item.startswith(ch):
   #        startswith.remove(item)
   #
   # return len(L) - len(startswith)
    
   startswith = L[:]

   for item in L:
        if not item.startswith(ch):
            startswith.remove(item)
   return len(startswith)

print("Question 4")
print(count_startswith(['rumba', 'salsa', 'samba'], 's'))

# 5 Correct
s = "av2sd34f"

# digits = ""
# for ch in s:
#     if ch.isdigit():
#         digits = digits + ch

# indices = []
# digits = ''

# for i in range(len(s)):
#     if s[i].isdigit():
#         indices.append(i)

# for index in indices:
#     digits = digits + s[index]

# digits = ''

# for i in range(len(s)):
#     if s[i].isdigit():
#         digits = digits + s[i]

digits = ''

for ch in s:
    if ch in '0123456789':
        digits = digits + ch

print("Question 5")
print(digits)

# 6 Incorrect
def is_one_to_one(d):
     """ (dict) -> bool

     Return True if and only if no two of d's keys map to the same value.
     
     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
     True
     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
     False
     >>> is_one_to_one({})
     True
     """
     
     # 1. Put all the values from d into a list
     # 2. For each value inlist, count how many times it appears in the list. If a value appears more than once in the list, return False
     # 3. Once all the values in the ;ist have been processed, return True because we  didn't see a duplicate value
     
     #  list = []
     #  for key in d:
     #      list.append(d[key])
     
     #  for item in list:
     #     if list.count(item) > 1:
     #         return False

     #  return True

     # 1. Use a list accumulator to keep track of the values we've seen so far
     # 2. For each key in d, if the value associated with that key has been seen, return False; otherwise, append it to the list of values that we've seen so far.
     # 3. Once all the keys have been processed, return True because we didn't see a duplicate value

     #  seen = []
     #  for key in d:
     #      if d[key] in seen:
     #          return False
     #      else:
     #          seen.append(d[key])
     #  return True

     # 1. Put all the values from d into a list
     # 2. Make a copy of that list
     # 3. Remove all the duplicate items from the second list
     # 4. Compare the lengths of the two lists. If they are equal, return True because that means that there were no duplicate items; otherwise, return False


print("Question 6")
print(is_one_to_one({'a': 1, 'b': 2, 'c': 3}))
print(is_one_to_one({'a': 1, 'b': 2, 'c': 1}))
print(is_one_to_one({}))

# 7 
def is_one_to_one(d):
    """ (dict) -> bool
 
    Return True if and only if no two of d's keys map to the same value.

    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """

    seen = []  # The values that have been seen so far.
    for k in d:
        if d[k] in seen:
             return False
        else:
            seen.append(d[k])
    return True

# 1. Use a list accumulator to keep track of the values we've seen so far
# 2. For each key in d, if the value associated with that key has already been seen, return False
#    Otherwise, append it to the list of values that we've seen so far.
# 3. Once all the keys have been processed, return True because we didn't see a duplicate value

# 8 Correct
# list of str, where each character is either 'Y' or 'N'
# dict of {int: str}

#9 
# list of [str, float] lists (ordered by time)
# dict of {str: float}
# Parallel lists: list of str and list of float (this is correct as well)

#10 Correct
# list of [str, float] lists (ordered by time)

#11 Correct
# a)
# 1. Build the weather dictionary.
# 2. Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 3. Create a dictionary where the keys are cities and the values are the sum of the precipitation amounts for that city for February.
# 4. Find the maximum value in that dictionary of city maximums.  The answer is the key associated with that maximum.

# b) 
# 1. Build the weather dictionary.
# 2. Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 3. Iterate through the cities in that dictionary, calculating the sum of the precipitation amounts for that city.  
# Keep track of the city that has the most precipitation so far.
# 4. Once the iteration is complete, whichever city had the most precipitation is the answer.

#12 Correct
# a)
# 1. Build the weather dictionary.
# 2. Iterate over the months to get each "city to precipitation" dictionary.  Make a "day to precipitation" dictionary 
# where the keys are all the days of the year from ('Jan', 1) through ('Dec', 31) and each value is a list of precipitation amounts for that day, one per city.
# 3. Iterate over the "day to precipitation" dictionary, making a list of the (month, day number) tuples 
# where the maximum precipitation among the cities for that day is 0. This is the "zero-precipitation" list.


# b)
# 1.Build the weather dictionary.
# 2. Create a "zero-precipitation" list containing all days of the year from ('Jan', 1) through ('Dec', 31)
# 3.Iterate over the months to get each "city to precipitation" dictionary. For each of these dictionaries:
# - For each city in the current "city to precipitation" dictionary, iterate over the precipitation amounts.  Because we know the current month and day number, we will remove from the "zero-precipitation" list any day that has a non-zero precipitation amount.
# - One this process is complete, the "zero-precipitation" list contains only the (month, day number) for days in which no city had precipitation.
