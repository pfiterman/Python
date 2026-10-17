num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# 1. print out each value on the list in sequential order
print("print sequential order")
for num in num_list:
    print(num, end=" ")

# 2. inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition
print("print greater than 45")
for num in num_list:
    if num>45:
        print(num, end=" ")

# 3. change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
print("print Over 45 or Under 45")
for num in num_list:
    if num>45:
        print("Over 45", end=" ")
    else:
        print("Under 45", end=" ")

# 4. Update the for loop to use the enumerate function so you can get and use the index. 
# Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number
print("print 36 and position")
for idx, num in enumerate(num_list):
    if num==36:
        print("Number found at position {}".format(idx))

# 5. Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
# 6. Inside the for loop increment the counter by 1.
# 7. Add a print statement outside the for loop to print the value of the count variable.
count = 0
for idx, num in enumerate(num_list):
    count += 1
    if num==36:
        print("Number found at position {}".format(idx))
        break
print(count)
