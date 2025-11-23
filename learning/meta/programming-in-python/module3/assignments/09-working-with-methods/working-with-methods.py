class A:
    def b(self):
        return "Function inside A"
class B:
    pass

class C:
    def b(self):
        return "Function inside C"

class D(B, C, A):
    pass

class D(C):
    pass

d = D()
print(d.b()) # Function inside C

class A:
    def c(self):
        return "Function inside A"

class B(A):
    def c(self):
        return "Function inside B"

class C(A,B): # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
    pass

class D(C):
    pass

d = D()
print(d.a)

class A:
    pass

class B(A):
    pass

class C(B):
    pass


c = C()
print(c.a()) # AttributeError: 'C' object has no attribute 'a'