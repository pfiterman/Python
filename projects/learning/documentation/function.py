def fib(n): # write fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# The interpreter recognizes the object pointed to by that name as a user-defined function.
# Other names can also point to that same function object and can also be used to access the function:
f = fib
f(100)

# you might object that `fib` is not a function but a procedure since it doesn’t return a value.
# In fact, even functions without a `return` statement do return a value, albeit a rather boring one.
# This value is called `None` (it’s a built-in name).
# Writing the value `None` is normally suppressed by the interpreter if it would be the only value written.
# You can see it if you really want to using `print()`:
fib(0)
print(fib(0))

# It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it
def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) # see below
        a, b = b, a+b
    return result

f100 = fib2(100) # call it
print(f100)      # write the result
