tup = ("a", 3, -0.2)

tup[0] # a
tup[1] # 3
tup[2] # -0.2

tup[-1] # -0.2
tup[:2] # ("a", 3)
tup[1:3] # (3, -0.2)

# Tuples are immutable
tup[0] = "b" # TypeError: "tupple" object does not support item assignment

# Check tuples methods
dir(tuple)  # Basically  it has just count and index methods

for item in tup:
    print(item)

len(tup) # 3

for i in range(len(tup)):
    print(tup[i])

tup1 = (1) 
print(tup1) # 1
tup1 = (1,)
print(tup1) # (1,)

