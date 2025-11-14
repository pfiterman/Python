# if else
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# checking for churros
for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)  

# checking for a desert that does not exits
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
    else:
        print('No sorry, that dessert is not on my list')

# break
for dessert in favorites:
    if dessert == 'Churros':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')


# continue
# Similar to break, continue can be used to control the iteration of the loop. 
# The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest. 
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

# pass
# The pass statement in this case acts as a placeholder, allowing you to include an empty block of code without causing a syntax error.
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
