# args you can pass any ammount of non keywords arguments
def sum_of1(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of1(4, 5, 6, 4, 5, 6))

# kwargs you can pass any amount of keywords arguments
def sum_of2(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum,2)
    

print (sum_of2(coffee=2.99, cake=4.55, juice=2.99))
