for i in range(10,13):
    for j in range(1, 5):
        print(i, j)

grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]

english = grades[0]
print(english) # [70, 75, 80]

total = 0
for mark in english:
    total = total + mark
average = total / len(english)
print(average)

def averages(grades):
    """ (list of list of number) -> list of float
    Return a new list in which each item is the average of the grades in the inner list at the corresponding position of grades

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    """
    averages = []
    for grades_list in grades:
        # Calculate the avreage of grades_list and append it to averages
        total = 0
        for mark in grades_list:
            total = total + mark
        averages.append(total / len(grades_list))
    return averages

print(averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]]))