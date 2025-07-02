input("What is your name? ")
name = input("What is your name? ")
print(name)

location = input("What is your location? ")
print(location)

print(name, "lives in", location)

num_coffee = input("how many cups of coffee? ") # returns str
print(num_coffee) # str '2' not int 2

'''hello''' # print multiple lines

print('''How
      are
      you?''')
#How
#are
#you?

# Escape sequences
s = '''How
are
You'''

print(s)  # 'How\nare\nyou?'    \n break line
print('3\t4\t5') # 3    4    5  \t tab
print('\\') # print sigle backlslash \
print('don\'t') # \' single quote
print("He says, \"Hi\".") # \" Hi\" escape double quotes
