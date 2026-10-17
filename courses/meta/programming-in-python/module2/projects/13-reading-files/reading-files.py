# read() - return the entire content as strings
with open("sample.txt", "r") as file:
    print(file.read(40)) # only the first 40 characters

# readdline() - return the single line as a string
with open("sample.txt", "r") as file:
    print(file.readline(10)) # number os characters of a single line

# readlines() - return the entire content as a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) # number os lines

    for line in lines:
        print(line)

with open("sample.txt", "r") as file:
    print(file.read(44))
    print(file.readline())
    data = file.readlines()

    for x in data:
        print(x)
