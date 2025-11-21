class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms) # 5
print(House.num_rooms) # 5

house.num_rooms = 7
print(house.num_rooms) # 7
print(House.num_rooms) # 5

# What has happened in the code above is, you have created an instance of a class called house and then modified the attribute for that instance 
# with a value of 7. It updates the value of the instance attribute, but not the class attribute. 
# So the num_rooms attribute of the class remains unchanged as 5, but the instance attribute associated with house object changes to 7. 
# Let's now insert an alternate piece of code in this. 

# This time, instead of an instance attribute, you will modify the class attribute by directly calling it over the class as follows:
House.num_rooms = 7
print(house.num_rooms) # 7
print(House.num_rooms) # 7

# Changes to a class attribute will affect all instances of the class, as they share the same class attribute unless overridden by an instance attribute. 
# Also note the use of the keyword self  in this example. self is a convention in Python, and you may use any other word in its place, 
# but as a practice, it is easy to recognize. self here is passed inside the method cost_evaluation() as it is an instance method 
# and facilitates the method to point to any instance of the House when that method is called. 
# It should be noted how any number of parameters can be passed to these instance methods but the first one is always the reference to the instance of that class.

