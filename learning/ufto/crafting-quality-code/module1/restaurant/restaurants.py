"""
A restaurant recommendation system

Here are some example dictionaries. These correspond to the information in data.txt

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 85,
 'Deep Fried Everything': 52}
 
 Price to list of restaurant names:
# dict of {str: list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str: list of str}
{"Canadian": ['Georgie Porgie'],
 "Pub Food": ['Georgie Porgie', 'Deep Fried Everything'],
 "Malaysian": ['Queen St. Cafe'],
 "Thai": ['Queen St. Cafe'],
 "Chinese": ['Dumplings R Us'],
 "Mexican": ['Mexican Grill']}

 With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we would produce this list:
 [[82, "Queen St. Cafe"], [71, "Dumplings R Us"]]
"""

# The file containing the restaurant data
FILENAME = "restaurants.txt"

def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of [int, str])

    Find restaurants in file that are priced according to price and that are tagged with any of the items in cuisines_list.
    Return a list of lists of the form [rating%, restaurant name], sorted by rating%    
    """

    # Read the file and build the data structures
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price
    names_matching_price = price_to_names[price]

    # New we have a list of restaurants in the right prince range
    # Need a new list of restaurants that serve one of the cuisines
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine
    # Need to look at rating and sort this list
    result = build_rating_list(name_to_rating, names_final)

    # We're done! Return that sorted list
    return result

def read_restaurants(file):
    """(file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$':[]}
    cuisine_to_names = {}

    with open(file, "r") as file:
        #Process 4 lines at once until the end of the file
        while True:
            name = file.readline().strip()
            if not name:
                break # End of file
            rating = file.readline().strip().replace('%', '')
            price = file.readline().strip()
            cuisines = [c.strip() for c in file.readline().strip().split(',')]
            file.readline()

            #Adding to name to rating dictionary
            name_to_rating[name] = rating

            #Adding to price to names dictionary
            if price not in price_to_names:
                price_to_names[price] = []
            price_to_names[price].append(name)

            #Adding to cuisines to names dictionary
            for cuisine in cuisines:
                if cuisine not in cuisine_to_names:
                    cuisine_to_names[cuisine] = []
                cuisine_to_names[cuisine].append(name)
            
    return name_to_rating, price_to_names, cuisine_to_names

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    >>> cuisines_to_names = {
        "Canadian": ['Georgie Porgie'],
        "Pub Food": ['Georgie Porgie', 'Deep Fried Everything'],
        "Malaysian": ['Queen St. Cafe'],
        "Thai": ['Queen St. Cafe'],
        "Chinese": ['Dumplings R Us'],
        "Mexican": ['Mexican Grill']
        }
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
        [[82, "Queen St. Cafe"], [71, "Dumplings R Us"]]
    """

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]
    Return a list of [rating%, restaurant name], sorted by rating%
    >>> name_to_rating = {
        'Georgie Porgie': 87,
        'Queen St. Cafe': 82,
        'Dumplings R Us': 85,
        'Deep Fried Everything': 52
    }
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names)
        [[82, "Queen St. Cafe"], [71, "Dumplings R Us"]]
    """