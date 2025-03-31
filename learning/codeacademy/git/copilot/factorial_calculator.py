def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def get_factorial_input():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    print("All tests passed")