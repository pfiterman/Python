# You can document your own functions using docstring
def area(base, height):                                              # Header
    '''(number, number) -> number                                    # Type contract

    Return the area of a triangle with dimensions base and height.   # Description

    >>> area(10, 5)
    25.0                                                             # Examples
    >>> area(2.5, 3)
    3.75
    '''
    return base * height / 2                                         # Body

def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degrees equivalent to Fahrenheit degrees

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0    
    '''
    return (fahrenheit - 32) * 5 / 9

def colder_temperature(temp1, temp2):
    '''(number, number) -> number

    Return the colder of the two temperatures, temp1 (degrees Celsius)
    and temp2 (degrees Fahrenheit), in degrees Celsius    
    '''
    temp2_celsius = convert_to_celsius(temp2)
    return min(temp1, temp2_celsius)

print(convert_to_celsius(32))
print(convert_to_celsius(212))