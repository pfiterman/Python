# Method Order Resolution
# Determines the order in which a given method or attribute passed is searched

# bottom to top
# left to right

# 1. ParentClass <- ChildClass
# MRO = fisrt ChildClass then ParentClass

# 2. Class Y           Class X
#       |________________|
#               |
#            Class Z
# MRO = Z then Y then X

# Depth-Fisrt search algorithm (DFS)
# C3 Linearization algorithm ( Python v.3 )

# C3 Linearization algorithm
# - Adheres to Monotonicity
# - Follow inheritance graph
# - Visits super class after local classes

# MRO attribute
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())