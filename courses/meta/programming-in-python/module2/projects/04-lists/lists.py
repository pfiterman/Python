list1 = [1,2,3,4,5]

list2 = ["A","B","C"]

list3 = ["Hello", 1, True, 40.22]

list4 = [1, [2,3,4], 5, 6]

print(*list1)
print(list1, sep= " ")

list1.insert(len(list1), 6)
print(list1, sep= " ")

list1.append(7)
print(list1, sep= " ")

list1.extend([8, 9, 10])
print(list1, sep= " ")

list1.pop(4)
print(list1, sep= " ")

del list1[2]
print(list1, sep= " ")

for x in list1:
    print("Value", x)