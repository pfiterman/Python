# open(<file_name> <file_location>, <mode>)
# modes:
# "r" - open and read (text format)
# "rb" - open and read (binary format)
# "r+" - open for reading and writing
# "w" - open for writing (overwrite existing files)
# "a" - open for editing or appending data

# close()
# with open("testing.txt", "r") as file:

file = open("test.txt", mode = "r")

data = file.readline()
print(data)

file.close()

with open("test.txt", mode = "r") as file:
    data = file.readline()
    print(data)