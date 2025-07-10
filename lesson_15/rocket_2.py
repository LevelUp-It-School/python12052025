from math import sqrt 

class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
        return distance

# rocket_0 = Rocket()
# rocket_1 = Rocket(10, 5)

# distance = rocket_0.get_distance(rocket_1)
# print(distance)

# class NewClass(ParentClass)

#     def __init__(self, arguments_new_class, arguments_parent_class):
#         super().__init__(arguments_parent_class)

# class Shuttle(Rocket):

#     def __init__(self, x=0, y=0, flights_completed=0):
#         Rocket.__init__(self, x, y)
#         self.flights_completed = flights_completed



from random import randint

class Shuttle(Rocket):

    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

# shuttle = Shuttle(10, 0, 3)
# print(shuttle)

shuttles = []

for x in range(0,3):
    x = randint(0, 100)
    y = randint(1, 100)
    flights_completed = randint(0, 10)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0, 100)
    y = randint(1, 100)
    rockets.append(Rocket(x, y))

for index, shuttle in enumerate(shuttles):
    print(f"Шатл {index} выполнил {shuttle.flights_completed} полетов")

print("\n")
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print(f"Растояние от первого шаттла до шаттла {index} равно {distance}")