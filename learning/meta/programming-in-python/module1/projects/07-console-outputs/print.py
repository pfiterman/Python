#comma separated
print(1, 2, 3) # 1 2 3

#arithmetic
print(1 + 3) # 4

#string concatenation
name = 'John'
print('Hello ' + name) # Hello John

# print parameters
print('Hello', 'you!', sep=', ') # Hello, you!

# direct formatting
a = 10
b = 5
ans = a + b

print('Adding the value of {} and {} = {}'.format(a,b, ans))
print('I like {0} more than {1}'.format("oranges","grapes"))
print('I like {1} more than {0}'.format("oranges","grapes"))