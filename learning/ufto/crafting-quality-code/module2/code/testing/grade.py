# 1 best choice of tests cases (Thinking about the Boundaries) - Correct
def high_low(guess, actual):
    """ (int, int) -> str

    Return "your guess is low" if guess is lower than actual, 
    "your guess is high" if guess is higher than actual, and
    "correct" if guess is equal to actual.

    >>> high_low(4, 10)
    "your guess is low"
    """
# guess refers to a value that is less than the value referred to by actual
# guess refers to a value equal to the value referred to by actual
# guess refers to a valu that is greater than the value referred to by actual

# 2 Think about the Size category for choosing test cases. - Correct
def first_two_items(L):
    """ (list of str) -> list of str

    Return the first two items in L. If there are fewer than
    two items in L, return all of the items.

    >>> first_two_items(["apple", "pear", "grape"])
    ["apple", "pear"]
    """
# []
# ["one"]
# ["one", "two"]
# ["one", "two", "three", "four"]

# 3 Consider this code Think about which test case category you might want to consider. - Incorrect
def is_preschooler(age):
    """ (int) -> bool

    Precondition: age >= 0

    Return True if and only if age is between 3 and 5 
    inclusive.

    >>> is_preschooler(4)
    True
    """

# one number between 0 and 2
# one number between 3 and 5
# one number over 5

# 4 Consider the Code: Which of these sets of values for  s and ch is the best choice of tests cases for this function - Correct
def count_occurrences(s, ch):
    """ (str, str) -> int

    Precondition: len(ch) == 1

    Return the number of occurrences of ch in s.

    >>> count_occurrences("hello", "l")
    2
    """

# s refers to ""  ch refers to "a"
# s refers to "a" ch refers to "a"
# s refers to "a" ch refers to "b"
# s refers to "abc" ch refers to "b"
# s refers to "abc" ch refers to "d"
# s refers to "abcabca" ch refers to "a"

# 5 Consider this code - Select the test(s) that reveal the bug. - Correct
def can_vote(age):
   """ (int) -> bool
 
   Precondition: age >= 0

   Return True if and only if a person aged age can vote
   in Canada. The legal voting age in Canada is 18 years and
   older.
   """
    
   return age > 18

# age refers to 18

# 6 Consider this code:
# There are bugs in the implementation of the function above (the code does not work as described). Select the test(s) that reveal the bugs.  
# (Think about the Order category for choosing test cases.) - Correct
def contains_item(L, s):
    """ (list, object) -> bool

    Return True if and only if s is an item of L.
    """

    for item in L:
        if item == s:
            return True
        else:
            return False

# L = [1,2,3]
# s = 3
# s = 2

# L = []
# s = 1
# print(contains_item(L,s))

# 7 Consider this code: - Correct
def sum_items(L):
    """ (list of number) -> number
  
    Return the sum of the items in L.
    """

    total = 0
 
    for item in L:
        total = item

    return total

# L = [1, 0, 1]
# L = [1, 2]
# print(sum_items(L))

# 8 Consider this code: - Correct
def can_afford(item_cost, wallet_money):
    """ (float, float) -> bool

    Return True if and only if wallet_money is greater or equal
    to item_cost.

    >>> can_afford(3.42, 10.00)
    True
    >>> can_afford(27.32, 5.00)
    False
    """

# test_can_afford

# 9 word.py - Correct
def word_frequency(letter_to_words):
    """ (dict of {str: list of str}) -> dict of {str: int}

    Precondition: the length of each list in letter_to_words
    is at least 1, each key in letter_to_words is a lowercase
    letter, and each value is a list of lowercase words
    beginning with that letter.

    Return a dictionary where the keys are the letters from
    letter_to_words, and the values are the number of words
    beginning with that letter in letter_to_words.

    >>> d = {'a': ['apple'], 'b': ['beet', 'banana'], 
       'c': ['carrot', 'cucumber']}
    >>> expected = {'a': 1, 'b': 2, 'c': 2}
    >>> word_frequency(d) == expected
    True
    """

# consider the unittest method header:def test_word_frequency(self):
# Select the unittest that are equivalent to the doctest in the word_frequencey docstring.  You can assume that words has been imported.
def test_word_frequency(self):
    """ A dictionary with several items."""

    # Add body here.
    # d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
    # actual = word_frequency(d)
    # expected = {'a': 1, 'b': 2, 'c': 2}
    # self.assertEqual(actual, expected)

    d = {'a': ['apple'], 'b': ['beet', 'banana'], 'c': ['carrot', 'cucumber']}
    actual = word_frequency(d)
    expected = {'c': 2, 'b': 2, 'a': 2}
    self.assertEqual(actual, expected)

# 10 Consider this code, which is in a file ecalled words.py
def make_uppercase(L):
    """ (list of str) -> NoneType

    Convert all letters in each string in L to uppercase.
    """

# Consider this unitest method header:
# Select the method body(ies) that correctly test the function with the list  ['Ada Lovelace', 'Grace Hopper', 'Alan Turing']
def test_make_uppercase(self):
    """ A list with several items."""

    # Add body here.
    L = ['Ada Lovelace', 'Grace Hopper', 'Alan Turing']
    actual = make_uppercase(L)
    expected = ['ADA LOVELACE', 'GRACE HOPPER', 'ALAN TURING']
    self.assertEqual(actual, expected)


