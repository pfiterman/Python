# Reload function
# Relaods an imported module in Python
# It allows make changes in your real code using import statements
import importlib
import filechanges

def chnages():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    chnages()
    input("it enter to reload...")