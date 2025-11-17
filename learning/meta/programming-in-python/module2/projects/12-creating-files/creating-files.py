try:
    with open("samples/newfile.txt", "w") as file:
        file.write("This is a new file created!")
        file.writelines(["\nThis is another line to be added", "\nAnd other line"])
except FileNotFoundError as e:
    print("ERROR", e)