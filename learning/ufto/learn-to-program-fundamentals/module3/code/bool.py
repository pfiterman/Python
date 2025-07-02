# Comparison Operators
lessthan = 3 < 4
print(lessthan) # True

greaterthan = 3 > 8
print(greaterthan) # False

greaterthan = 8 > 3
print(greaterthan) # True

greaterthan = 3.5 >= 3.4
print(greaterthan) # True

equal = 7 == 7
print(equal) # True

equal = 7 == 7.0
print(equal) # True

x = 7
y = 8
equal = x == y # False

notequalto = 3 != 4
print(notequalto) # True

# Logical Operators
grade = 80
greaterthan = grade >= 50 # True
not_operator = not (grade >= 50) # False
not_operator = not not (grade >=50) # True

grade2 = 70
and_operator = (grade > 50) and (grade2 >= 50) # True
grade = 40
and_operator = (grade > 50) and (grade2 >= 50) # False
grade = 80
grade2 = 40
and_operator = (grade > 50) and (grade2 >= 50) # False

grade = 70
grade = 80
or_operator = (grade > 50) and (grade2 >= 50) # True
grade = 40
or_operator = (grade > 50) and (grade2 >= 50) # True
grade = 80
grade2 = 40
or_operator = (grade > 50) and (grade2 >= 50) # True

grade = 80
grade2 = 90
exp1 = not grade >=50 or grade2 >= 50 # True
exp1 = (not grade >=50) or grade2 >= 50 # True
exp2 = not (grade >=50 or grade2 >= 50) # False
exp3 = (4 != 4) or ( 2 > 3) # False
exp3 = 4 != 4 or  2 > 3 # False

