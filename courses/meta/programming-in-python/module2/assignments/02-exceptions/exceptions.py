# Your task in this exercise is to add code to trap exceptions and handle them in a more user-friendly way. 

# IndexError
items = [1,2,3,4,5]
try:     
    item = items[6]
    print(item)
except IndexError as e:
    print("Something went wrong!", e)


# ZeroDivisionError
def divide_by(a, b):   
    try:
        return a / b
    except ZeroDivisionError: 
        return 0
    except Exception as e:
        print(e, "Something went wrong!")
    
ans = divide_by(10, 0)
print(ans)

# FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")