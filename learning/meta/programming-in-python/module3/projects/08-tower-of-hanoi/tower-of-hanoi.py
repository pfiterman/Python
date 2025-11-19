# Introduction

# The Tower of Hanoi is a popular puzzle in mathematics and programming. 
# It's widely considered as a good way to demonstrate recursion. 
# There is a legend about an ancient Hindu temple containing a large room with three posts surrounded by 64 golden disks. 
# The puzzle was presented to a young priest who was told to move all the disks from one post to another without violating a set of given rules. 
# By estimates, if the priest followed the rules and moved one disk per second, the puzzle would be solved in 2^64 – 1 second. 
# That's about 585 billion years. By then the temple would no longer exist. 
# Inspired by this legend, a French mathematician Edouard Lucas invented the Tower of Hanoi puzzle more than a hundred years ago.

# Objective and rules of the puzzle

# The objective is to move n number of disks from one tower to another following a set of rules. These rules are as follows: 
# 1. Only one disk can be moved at a time 
# 2. Only the upper disk of any of the towers can be moved 
# 3. Larger disks cannot be placed over smaller disks

# In the optimal scenario of solving the puzzle, the total moves will be 2^n – 1 where n is the number of disks that need to be moved.
# Now let's examine how you can write code for this in Python using the principles of recursion that you have learned.

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself.
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code: Initializing and calling the function
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')