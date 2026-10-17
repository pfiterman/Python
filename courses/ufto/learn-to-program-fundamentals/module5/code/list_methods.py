colours = []
prompt = "Enter another one of your favourite colours (type return to end): "

colour = input(prompt) # ["yellow", "blue", "brown"]
while colour != "":
    colours.append(colour)
    colour = input(prompt)

colours.extend(["hot pink", "neon green"])
print(colours) # ["yellow", "blue", "brown", "hot pink", "neon green"]

colours.pop() # remove last element and return it
print(colours) # ["yellow", "blue", "brown", "hot pink"]

print(colours.pop(2)) # brown

# colours.remove("black") # ValueError remove the first ocorrence object

if colours.count("yellow") > 0:
    colours.remove("yellow") 

print(colours)  # ["blue", "hot pink"]

if "yellow" in colours:
    colours.remove("yellow")

print(colours) # ["blue", "hot pink"]

colours.extend(['auburn', 'taupe', 'magenta']) # ["blue", "hot pink", "auburn", "taupe", "magenta"]
colours.sort()
print(colours) # ["auburn", "blue", "hot pink", "magenta", "taupe"]

colours.reverse()
print(colours) # ["taupe", "magenta", "hot pink", "blue", "auburn"]

colours.insert(-2, "brown")
print(colours) # ["taupe", "magenta", "hot pink", "brown", "blue", "auburn"]

# colours.index("neon green") # ValueError is not in the list
if "hot pink" in colours:
    where = colours.index("hot pink")
    colours.pop(where)

print(colours) # ["taupe", "magenta", "brown", "blue", "auburn"]