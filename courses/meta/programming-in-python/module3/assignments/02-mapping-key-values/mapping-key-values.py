a = [[96], [69]]
print(''.join(list(map(str,a))))

z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)