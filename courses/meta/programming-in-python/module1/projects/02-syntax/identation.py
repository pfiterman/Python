# functions allow you to group code into reusable blocks.
# def keyword: In Python, the def keyword defines a function. 

def function_name(parameters):
    # This is inside the function body
    result = "result"
    return result

# function_name: The name you give to the function.
# return: Optional statement to send back a result from the function.
# parameters: Optional values passed to the function. It can be one or more.

# correct indented code
def say_hello():
    print("Hello there!")

print(say_hello())

# correct non-indented code
def say_hello(): print("Hello there!")

print(say_hello())

# incorrect
'''
def say_hello():
print("Hello there!")

    def say_hello():
print("Hello there")
'''