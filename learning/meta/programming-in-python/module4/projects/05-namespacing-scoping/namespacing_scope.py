# Namespace
# Mapping for Names and Objects

# Scope resolution: LEGB rule
# 1. Local
# 2. Enclosed
# 3. Global
# 4. Built-In

greek = "alpha"
print("Global declaration: " + greek, id(greek))

def b():
    Greek = "beta"
    print("Inside local: " + Greek, id(Greek))

def c():
    greek = "gamma"
    print("Enclosed: " + greek, id(greek))

c()
print("Inside local: End of local scope: " + greek, id(greek))

b()
print("Global after local execution: " + greek, id(greek))

# Local and global scope
country = "USA"
print("Country name: " + country)
print(globals())
print("--------------")

def b():
    country = "Germany"
    print("Country name: " + country)
    print(locals())

b()
print("Country name: " + country)


def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: " + animal)
    
    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal)

animal = "camel"
d()
print("Global animal: " + animal)