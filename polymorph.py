class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        print('The dog is running')

class Bird(Animal):
    def move(self):
        print('The bird is flying')

class Fish(Animal):
    def move(self):
        print('The fish is Swimming')

class Car:
    def move(self):
        print('The car is driving')

class Boat:
    def move(self):
        print('The Boat is Sailing')

# creating instance for animal and vehicle
animals = [Dog(), Bird(), Fish()]
vehicles = [Car(), Boat()]

# iterate over animals and vehicles 
for animal in animals:
    animal.move()

for vehicle in vehicles:
    vehicle.move()