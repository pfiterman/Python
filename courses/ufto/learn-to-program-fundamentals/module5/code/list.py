grades = [80, 90, 70]
grades[0] # 80
grades[1] # 90
grades[2] # 70

grades[1:2] # [90]
grades[0:2] # [80, 90]

exp1 = 80 in grades # True
exp2 = 60 in grades # False

len(grades) # 3
min(grades) # 70
max(grades) # 90
sum(grades) # 240

subjects = ["bio", "cs", "math", "history"]
len(subjects) # 4
min(subjects) # bio
max(subjects) # math
#sum(subjects) # TypeError unsupported operand

street_address = [10, "Main Street"]
for grade in grades:
    print(grade)

for item in subjects:
    print(item)