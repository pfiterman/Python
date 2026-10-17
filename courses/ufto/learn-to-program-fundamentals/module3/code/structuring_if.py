grade1 = 70
grade2 = 80

if grade1 >= 50:
    print("You passed a course with grade: ", grade1)
elif grade2 >= 50:
    print("You passed a course with grade: ", grade2)

if grade1 >= 50:
    print("You passed a course with grade: ", grade1)
if grade2 >= 50:
    print("You passed a course with grade: ", grade2)

precipitation = True
temperature = +8

if precipitation:
    if temperature > 0:
        print("Bring your umbrella!")
    else:
        print("Wear boots and winter coat!")

if precipitation and temperature > 0:
    print("Bring your umbrella!")
elif precipitation:
    print("Wear boots and winter coat!")