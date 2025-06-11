from collections import Counter

def is_one_to_one(d):
    """ dict of (str : int) -> bool

    Return True if and only if no two of d's keys map to the same value

    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """

    list = []
    for value in d.values():
        list.append(value)
    
    ocurrences = Counter(list)
    for i in range(len(ocurrences)):
        if ocurrences[i]>1:
            return False
    
    return True


