def convert_to_celsius(fahrenheit):
    """
    Convert a fahrenheit temperature to celsius
    
    :param fahrenheit: Temperature in fahrenheit
    """
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def weather_info(fahrenheit):
    """ (number) -> str

    Return if temperature is freezing or is above freezing

    is freezing when <= 0 celsius
    is abobe freezing when > 0 celsius

    >>> weather_info(50)
    10.0 is above freezing temperature

    >>> weather_info(23)
    -5.0 is freezing temperature
    """
    celsius = convert_to_celsius(fahrenheit)
    status = "freezing" if celsius < 0 else "above freezing"
    return f"{celsius} is {status} temperature"

