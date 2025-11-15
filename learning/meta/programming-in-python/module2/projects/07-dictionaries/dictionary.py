# dictionary is key:value pairs
sample_dict = {1: "Coffee", 2: "Tea", 3: "Juice"}
print(sample_dict[1])

sample_dict[2] = "Mint Tea"
print(sample_dict[1])

del sample_dict[3]

my_d = {}
print(type(my_d))

my_d = {1: "Test", "Name": "Jim"}
print(my_d[1])
print(my_d["Name"])

my_d[2] = "Test 2"
my_d[1]= "Not a test!"
print(my_d)

del my_d[1]
print(my_d)

#printing the keys
for x in my_d:
    print(x)

#to access keys and values use items()
for key, value in my_d.items():
    print(str(key) + " : " + value)