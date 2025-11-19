# recursion
# It's essentially a funtion that calls itself

# It's used for:
# 1. repetitive problems
# 2. complex structures

def example(obj):
    #some logic
    return example(obj)

# It's like a for-loop, but you must always handle the results to avoid an infinite loop

def factorial_by_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial=factorial*i
        return factorial
    
print(factorial_by_looping(5))

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
print(factorial_recursive(5))

# factorial_recursive(5)
# = 5 * factorial_recursive(4)
# = 5 * (4 * factorial_recursive(3))
# = 5 * (4 * (3 * factorial_recursive(2)))
# = 5 * (4 * (3 * (2 * factorial_recursive(1))))
# = 5 * (4 * (3 * (2 * 1)))
# = 5 * (4 * (3 * 2))
# = 5 * (4 * 6)
# = 5 * 24
# = 120

# Advantages
# 1. Neat code
# 2. Tasks can break in easy to read sub-problems
# 3. Easy sequences

# Disadvantages
# 1. Hard to follow
# 2. Expensive and memory and sometimes inefficient 
# 3. Difficult to debug