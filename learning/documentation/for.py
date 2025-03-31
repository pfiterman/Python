# Measure some string:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

class User:
    def __init__(self, user, status):
        self.user = user
        self.status = status

class Users:
    def __init__(self, iterable):
        self.items = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items.append(item)

    __update = update #private copy of original update() method


user1 = User('pfiterman','active')
user2 = User('nshademan','inactive')
users = Users([user1, user2])

# Strategy: Iterate over a copy
for user, status in users.copy.items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
