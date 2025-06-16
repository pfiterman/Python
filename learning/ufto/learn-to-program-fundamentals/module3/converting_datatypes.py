str = str(3)
str = str * 10 # '3333333333'
number = int(str * 5) # 33333
str = str(number) # '33333'
str = str(4.65) # '4.65'

int = int('456') # 456
float = float('456') # 456.0
int = int('I have 7 apples') # ValueError

shoes = input("Enter the numebr of shoes: ") # Let's say user typed 863
print(shoes) # '863'
shoes1 = 627
shoes2 = int(input("Enter the numebr of shoes: ")) # Let's say user typed 627
exp = shoes1 == shoes2 # True