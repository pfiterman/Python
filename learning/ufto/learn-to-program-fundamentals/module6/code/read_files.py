# Using While
flanders_filename = "D:\\Developer\\Python\\learning\\ufto\\learn-to-program-fundamentals\\module6\\flanders_fields.txt"
flanders_file = open(flanders_filename, "r")

print(flanders_file.readline())
print(flanders_file.readline())

flanders_file.close()

flanders_file = open(flanders_filename, "r")
line = flanders_file.readline()
while line != "":
    print(line)
    line = flanders_file.readline()

flanders_file.close()

flanders_file = open(flanders_filename, "r")
line = flanders_file.readline()
while line != "":
    print(line, end="")
    line = flanders_file.readline()

flanders_file.close()

flanders_file = open(flanders_filename, "r")
line = flanders_file.readline()
line = flanders_file.readline()
line = flanders_file.readline()
print(line)

while line != "\n":
    print(line)
    line = flanders_file.readline()

flanders_file.close()

# Using For Loops
flanders_file = open(flanders_filename, "r")
for line in flanders_file:
    print(line, end="")

flanders_file.close()

# For small files - not huge
flanders_file = open(flanders_filename, "r")
print(flanders_file.read())

flanders_file.close()

# Using readlines
flanders_file = open(flanders_filename, "r")
flanders_file.readlines()
flanders_file.close()

flanders_file = open(flanders_filename, "r")
lines = flanders_file.readlines()
for line in lines:
    print(line, end="")

flanders_file.close()

print(lines[0])
print(lines[1])
print(lines[2])