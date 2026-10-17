# and - check for both conditions to be true
a = 8
b = 12
cond = a>5 and a<10

# or - check for at least one condition to be true
cond = a>5 or b>10

# not - return false if the result it true
cond = not(a>5)

a = True
b = True

if a and b:
    print("All true!");
if a or b:
    print("At least one is true")
if not(a) or not(b):
    print('At least one is true')