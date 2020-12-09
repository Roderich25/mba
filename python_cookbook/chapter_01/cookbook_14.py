

# 1.14 Sorting objects without native comparison support

from operator import attrgetter


class User:

    def __init__(self, user_id, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.user_id},'{self.first_name}','{self.last_name}')"


users = [
    User(99, 'Rodrigo', 'Solis'),
    User(23, 'Rodrigo', 'Avila'),
    User(53, 'Pablo', 'Avila'),

]
print(sorted(users, key=lambda u: u.user_id))
# lambda expression is alittle bit slower than `attrgetter`
print(sorted(users, key=attrgetter('user_id')))


# another example
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(by_name)

# another example
min_user = min(users, key=attrgetter('user_id'))
max_user = max(users, key=attrgetter('user_id'))
print(min_user)
print(max_user)
