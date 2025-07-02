#1 returns True
dollars = 8
dollars == 8.0
8 >= dollars

#2 returns True
cents = 34
not not cents >= 33
cents < 8 or cents > 3

#2 returns True
instructors = 2
exp1 = not instructors < 1
exp2 = not not instructors >= -3
# print(exp1)
# print(exp2)

#3 returns True
dollars = 18
cents = 53
exp1 = dollars == 10 or not cents != 53 
exp2 = dollars == 18 or not cents == 53
exp3 = not dollars < 10 and cents > 15

print(exp1)
print(exp2)
print(exp3)

#4 equivalent to 8 > x >= 5
# 8 > x and x >=5 

#5 int(99.9) produce?
result = int(99.9)
# print(result) # 99

#6 eggs % 12 == 0 ... select equivalent
# return not eggs % 12 == 0
# return eggs % 12 != 0 

#7 consider code
#age1 = input("How old are you? ")
#age2 = input("How old is your best friend? ")

# x = int(age1)
# y = int(age2)
# print (str(x + y))

# print(int(age1) + int(age2))

#8 
# math.factorial

#9
# import question

#10 what's printed?
# slow

#11 what's printed?
# None

#12 which expression returns 'pass'
# grade_report(70)
# grade_report(50)

#12 which expression returns 'warm enough for ice cream'
# weather_report(20)
# weather_report(30)

#13 grade1 and grade2 
# passing_grade >= 50
# must return 0.0 if neither grade is a passing grade
# the passsing grade if exactly one grade is a passing grade
# average of the two grades if both are passing grades.
grade1 = 40.0
grade2 = 80.0

total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)

#14 code visualizer
# 1 frame including global

#15 code visualizer
# 3 frames including global

# 16 code visualizer
# 3 frames including global