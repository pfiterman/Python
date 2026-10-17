print("hello")
print(3 + 7 -3)
print("hello", "there") # hello there

def square_return(num):
    return num ** 2

def square_print(num):
    print("The square of num is", num ** 2)

answer_return = square_return(4) # returns 16
print(answer_return)

answer_print = square_print(4)   # returns None
print(answer_print)

calc1 = answer_return * 5  # return 80 -> 16 * 5
calc2 = answer_print * 5 # TypeError: unsupported operand typoe(s) for *: 'NoneType' and 'int'