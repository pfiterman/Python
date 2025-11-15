#global scope
my_global = 10

def fn1():
    enclosed_v = 8
    def fn2():
        local_v = 5
        print("Access to Global", my_global)
        print("Access tp enclosed", enclosed_v)
    fn2()

# print(enclosed_v) - just accessible on fn1 local scope
# print(local_v) - just accessible on fn2 local scope