# 1 How many times is function print called - Correct
for i in range(2):
    for j in range(3):
        print(f"printed {j}")

# m * n

# 2 How many times function print is called - Correct
for i in range(3):
    print(i)

for j in range(4):
    print(j)

# m + n

# 3 - Correct
# Approach 1:
L = list(1001)
for i in range(len(L)):
    for j in range(len(L)):
        # do a few assignment statements to accomplish the task.
        print(j)

# Approach 2:
for i in range(1000):
    for j in range(len(L)):
        # do a few assignment statements to accomplish the task.
        print(j)

# When L has more than 1000 items

# 4 Question 4  For linear search, if we are searching for 7 , which list will cause the fewest number of iterations? - Correct
# [7, 6, 5, 4, 3, 2]

# 5 Question 5 The list  [4, 2, 5, 6, 7, 3, 1] is shown below after each pass of a sorting algorithm - Correct
# [1, 2, 5, 6, 7, 3, 4]
# [1, 2, 5, 6, 7, 3, 4]
# [1, 2, 3, 6, 7, 5, 4]
# [1, 2, 3, 4, 7, 5, 6]
# [1, 2, 3, 4, 5, 7, 6]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]

# selection sort

# 6 The list  [4, 2, 5, 6, 7, 3, 1] is shown below after each pass of a sorting algorithm - Correct
# [2, 4, 5, 6, 3, 1, 7]
# [2, 4, 5, 3, 1, 6, 7]
# [2, 4, 3, 1, 5, 6, 7]
# [2, 3, 1, 4, 5, 6, 7]
# [2, 1, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]

# buble sort

# 7 The list  [4, 2, 5, 6, 7, 3, 1] is shown below after each pass of a sorting algorithm: - Correct
# [4, 2, 5, 6, 7, 3, 1]
# [2, 4, 5, 6, 7, 3, 1]
# [2, 4, 5, 6, 7, 3, 1]
# [2, 4, 5, 6, 7, 3, 1]
# [2, 4, 5, 6, 7, 3, 1]
# [2, 3, 4, 5, 6, 7, 1]
# [1, 2, 3, 4, 5, 6, 7]

# insertion sort

# 8 List [1, 5, 8, 7, 6, 1, 7] is being sorted using selection sort.  Here is what the list will look like after each of the first three passes: - Correct
# [1, 5, 8, 7, 6, 1, 7]
# [1, 1, 8, 7, 6, 5, 7]
# [1, 1, 5, 7, 6, 8, 7]

# What will the list look like after the 4th pass?
# [1, 1, 5, 6, 7, 8, 7]

# 9 List [6, 8, 2, 1, 1, 9, 4] is being sorted using insertion sort.  Here is what the list will look like after each of the first three passes: - Correct
# [6, 8, 2, 1, 1, 9, 4]
# [6, 8, 2, 1, 1, 9, 4]
# [2, 6, 8, 1, 1, 9, 4]

# What will the list look like after the 4th pass?
# [1, 2, 6, 8, 1, 9, 4]

# 10 In bubble sort on the first pass through the list, which item gets moved to the far right? - Correct
# the largest item

# 11 Here is the code for function insert with docstring and comments removed - Correct
def insert(L, i):
    value = L[i]

    j = i
    while j != 0 and L[j - 1] > value:
        L[j] = L[j - 1]
        j = j - 1

    L[j] = value

# In the following list, there is an x in color black.  In this question, you will choose a value for that variable.
# L = [2, 5, 6, 7, 8, x, 4]
# The first 5 items are sorted

# If we call  insert(L, 5) that unknown value will be inserted into the sorted section, growing the sorted section by 1 item.  
# Select a value for x that would be moved all the way to index 0 in the list.

# Answer: 1

# 12 Here is the code for function insert with docstring and comments removed - Correct
def insert(L, i):
    value = L[i]

    j = i
    while j != 0 and L[j - 1] > value:
        L[j] = L[j - 1]
        j = j - 1

    L[j] = value

# In the following list, there is an x in color black.  In this question, you will choose a value for that variable.
# L = [2, 5, 6, 7, 8, x, 4]
# The first 5 items are sorted

# If we call  insert(L, 5) that unknown value will be inserted into the sorted section, growing the sorted section by 1 item.  
# Select a value for x that would not move

# Answer: 9

# 13 Here is the code for function insert with docstring and comments removed - Incorrect
def insert(L, i):
    value = L[i]

    j = i
    while j != 0 and L[j - 1] > value:
        L[j] = L[j - 1]
        j = j - 1

    L[j] = value

# The while loop can be terminated for one of two reasons: j == 0 or  L[j - 1] <= value L[j - 1].  
# In which situation does the loop terminate because  j == 0?

# Answer: When the item at index is neither smaller not larger than everything in the sorted section

# 14 Here is the code for function insert - Incorrect
def insert(L, i):
    value = L[i]

    j = i
    while j != 0 and L[j - 1] > value:
        L[j] = L[j - 1]
        j = j - 1

    L[j] = value

# For function call  insert(L, i), in the worst case, the item at index i is moved all the way to index  0.  
# Variable j starts off at i and is decreased by 1 on each iteration of the while loop until it reaches 0.  
# In this worst-case situation, how many times is the body of the while loop executed?

# Answer: i + 1

# 15 Here is the code for function insertion_sort: - Correct
def insertion_sort(L):
    for i in range(len(L)):
        insert(L, i)

# This question is about the worst-case running time for this code.  (The worst case for insertion sort happens when a list is sorted in reverse, from largest to smallest.)
# - On the first iteration of this loop,  i refers to  0, so  insert(L, 0) is called, and the while loop in function insert iterates 0 times.
# - On the second iteration,  insert(L, 1) is called, and the while loop in function  insert iterates 1 time.
# - On the last iteration,  insert(L, len(L) - 1) is called, and the while loop in function  insert iterates  len(L) - 1 times.

# In total, how many times is the body of the while loop in function insert executed during one call on function insertion_sort?

# Answer: 0 + 1 + ... + len(L) - 1

# 16 In the worst case, on a call on function  insertion_sort(L), the total number of times the loop body in function  insert is executed is this: - Correct
# 0 + 1 + 2 + 3 + ... + (len(L) - 3) + (len(L) - 2) + (len(L) - 1)

# The 0 doesn't affect the sum, so we can simplify to this:
# 1 + 2 + 3 + ... + (len(L) - 3) + (len(L) - 2) + (len(L) - 1)

# We can add the first and last items together, and the second and second-last items together, and so on:
# 1 + (len(L) - 1)    # The 1 and the -1 cancel, leaving len(L)
# 2 + (len(L) - 2)    # The 2 and the -2 cancel, leaving len(L)
# 3 + (len(L) - 3)    # The 3 and the -3 cancel, leaving len(L)+ ...

# Every line in the equation adds up to  len(L).  
# Roughly how many lines in the equation are there, and what is the total number of times the loop body is executed?  
# (Hint: work this out using a smaller example, such as a length 9 list, and then generalize.)

# Answer: Len(L) / 2
# Len(L) * Len(L) / 2

# 17 For a call on function  insertion_sort(L), in the worst case, select the running time: - Correct
# Quadratic in the length of list L

# 18 For a call on function insertion_sort(L) , in the best case (where list L is already sorted), how many times is the body of the while loop in function insert executed?
# Answer: Len(L) - Incrrect