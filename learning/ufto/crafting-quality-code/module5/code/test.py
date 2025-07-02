def double_values(D={'a': 1}):
    """(dict of {str: int}) -> NoneType
    Double each value in D, and print D.
    """
    
    for key in D:
        D[key] = D[key] * 2
    print(D)

# The default parameter values are assigned when the function definition is executed. When a call on double_values changes D, that change persists from one
# function call to the next

double_values()
double_values()
double_values()


def raise_an_exception(v):
    raise ValueError(
        "{} is not a valid value.".format(v))

def main():
    raise_an_exception(3)

if __name__ == '__main__':
    try:
        main()
    except ValueError as ve:
        print(ve)