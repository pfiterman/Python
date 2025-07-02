grades = [["A1", 80], ["A2", 70], ["A3", 90]]

grades[0] # ["A1", 80]
grades[1] # ["A2", 70]
grades[2] # ["A3", 90]

grades[1][0] # A2
grades[1][1] # 70

asn_to_grade = {
    "A1": 80,
    "A2": 70,
    "A3": 90
}

asn_to_grade["A2"] # 70
# asn_to_grade["A4"] # KeyError

exp1 = "A4" in asn_to_grade # False
exp2 = "A2" in asn_to_grade # True
exp3 = 80 in asn_to_grade # False

len(asn_to_grade) # 3

# lists and dictionaries are mutable
asn_to_grade["A4"] = 85

# asn_to_grade = {
#     "A1": 80,
#     "A2": 70,
#     "A3": 90,
#     "A4": 85
# }

len(asn_to_grade) # 4

asn_to_grade["A4"] = 90
print(asn_to_grade) # {"A1": 80, "A3": 90, "A2": 70, "A4": 90}

# remove from the dictionary
del asn_to_grade["A4"]
print(asn_to_grade) # {"A1": 80, "A3": 90, "A2": 70}

for key in asn_to_grade:
    print(key)

for key in asn_to_grade:
    print(asn_to_grade[key])

for key in asn_to_grade:
    print(key, asn_to_grade[key])

# Empty dictionary
d = {}
len(d) # 0
d = {"apple": 2, 5: 8}

# Key must be immutable
# You can't associate a list as a key because list is mutable
d[[1,2]] = "banana" # TypeError: unhashable type: "list"

# However you can associate tuples as key (tuple is immutable)
d[(1,2)] = "banana"