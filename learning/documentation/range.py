# range(stop)
# range(start, stop[, step])

# This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. 
# The arguments must be plain integers. If the step argument is omitted, it defaults to 1. 
# If the start argument is omitted, it defaults to 0. 
# The full form returns a list of plain integers [start, start + step, start + 2 * step, ...]. 
# If step is positive, the last element is the largest start + i * step less than stop; 
# if step is negative, the last element is the smallest start + i * step greater than stop. 
# step must not be zero (or else ValueError is raised). Examples:

range_10 = []
for i in range(10):
    range_10.append(i)
print(f"range(10) = {range_10}") 

range_5_10 = []
for i in range(5, 10):
    range_5_10.append(i)
print(f"range(5, 10) = {range_5_10}")    

range_0_10_3 = []
for i in range(0, 10, 3):
    range_0_10_3.append(i)
print(f"range(0, 10, 3) = {range_0_10_3}")

range_negative = []
for i in range(-10, -100, -30):
    range_negative.append(i)
print(f"range(-10, -100, -30) = {range_negative}")

list = ['Mary', 'had', 'a', 'little', 'lamb']
new_list = []
for i in range(len(list)):
      new_list.append(list[i])
print(f"new_list = {new_list}")

sum_range = sum(range(4))
print(f"sum(range(4)) = {sum_range}")

