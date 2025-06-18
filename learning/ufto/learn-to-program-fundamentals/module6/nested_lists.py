grades = [["Assignment 1", 80], ["Assignment 2", 90], ["Assignment 3", 70]]
len(grades) # 3

grades[0] # ["Assignment 1", 80]
grades[1] # ["Assignment 2", 90]
grades[2] # ["Assignment 3", 70]

for item in grades:
    print(item)

grades[0][0] # "Assignment 1"
grades[0][1] # 80
grades[1][0] # "Assignment 2"
grades[1][1] # 90
grades[2][0] # "Assignment 3"
grades[2][1] # 70

def calculate_average(asn_grades):
    """ (list of list of [str, number]) -> float
     Return the average of the grades in asn_grades.

     >>> calculate_average([["A1", 80], ["A2", 90]])
     85.0
    """
    total = 0
    for item in asn_grades:
        total = total + item[1]
    return total / len(asn_grades)

print(calculate_average([["A1", 80], ["A2", 90]]))