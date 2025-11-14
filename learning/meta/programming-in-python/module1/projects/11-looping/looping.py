# For
str = "Looping"

for item in str:
    print(item)

favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]

for item in favorites:
    print('I like this desert ',item)

for idx, item in enumerate(favorites):
    print(idx, item)


# While
count = 0
while count < len(favorites):
    print('I like this desert', favorites[count])
    count += 1

