# any ammount of whitespace on a single line is ok
x     =        1        +        2
print(x) #3

# breaking line is incorrect
x = 1
+ 2
print(x) #1

# you can use the "\" though 
x = 1 \
+ 2 \
+ 3
print(x) #6