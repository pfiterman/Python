import tkinter.filedialog

# 1
def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [6, 15, 24]

# 2
def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')  # 2 times

# 3 
def mystery(s):
    """ (str) -> bool

    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)

mystery("madam") 
# for 0 to 1
# s[0] == s[4] True
# s[1] == s[3] True
# Return True if only if s is equal to the reverse of s (palidrome)

# 4
def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    L[0] = last_item
    return L

print(shift_right(["a","b","c","d","e"])) # ["e", "a","b","c", "d"]

# 5
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with the string from thecorresponding position of list1 and the int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    # for i in range(len(list1)):
    #     inner_list = []
    #     inner_list.append(list1[i])
    #     inner_list.append(list2[i])
    #     pairs.append(inner_list)
    
    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))  # the commented code and the current one

# 6
# values[1][1]

# 7
# breakfast[-2][-2]

# 8
# 15 times

# 9
def contains(value, lst):
   """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
   True
   """
   found = False  # We have not yet found value in the list.

   # CODE MISSING HERE
   # for sublist in lst:
   #     if value in sublist:
   #         found = True
   
   for i in range(len(lst)):
       for j in range(len(lst[i])):
          if lst[i][j] == value:
               found = True

   return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))

# 10
# The readline approach

# 11 
# data_file refers to a file open for reading.
# from_filename = tkinter.filedialog.askopenfilename()
# from_file = open(from_filename, "r")

# data_file refers to a file open for reading.
# for line in from_file:
#      print(line.rstrip("\n"))
#      print(line.strip())

# from_file.close()

# 12
def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter. 
     The lines should have the new line removed.

    Precondition: len(letter) == 1
    """

    matches = []

    # CODE MISSING HERE
    # for line in file:
    #     if line.startswith(letter):
    #         matches.append(line.rstrip('\n'))

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
    return matches

# from_filename = tkinter.filedialog.askopenfilename()
# from_file = open(from_filename, "r")
# print(lines_startswith(from_file, "I"))

# 13
def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
    # for s in sentences:
    #     file.write(s)
    #     file.write('\n')

    for s in sentences:
        file.write(s + '\n')


# to_filename = tkinter.filedialog.asksaveasfilename()
# to_file = open(to_filename, "w")
# print(write_to_file(to_file, ["this", "sentence", "must", "be", "added", "to", "file"]))