"""
Python Inheritance Demonstration
-------------------------------
This file demonstrates:
1. Single inheritance
2. Multilevel inheritance
3. Multiple inheritance
4. Hierarchical inheritance
5. Method overriding

Run:
    python inheritance.py
"""


# 1. Single Inheritance
class Animal:
    def eat(self):
        print("Animals can eat.")


class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


# 2. Multilevel Inheritance
class Vehicle:
    def start(self):
        print("The vehicle has started.")


class Car(Vehicle):
    def drive(self):
        print("The car is moving.")


class ElectricCar(Car):
    def charge(self):
        print("The electric car is charging.")


# 3. Multiple Inheritance
class Camera:
    def take_photo(self):
        print("Photo captured.")


class MusicPlayer:
    def play_music(self):
        print("Playing music.")


class Smartphone(Camera, MusicPlayer):
    pass


# 4. Hierarchical Inheritance
class Shape:
    def describe(self):
        print("This is a shape.")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle.")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle.")


# 5. Method Overriding
class Employee:
    def work(self):
        print("The employee is working.")


class Developer(Employee):
    def work(self):
        print("The developer is writing code.")


def main():
    print("\n--- 1. Single Inheritance ---")
    dog = Dog()
    dog.eat()
    dog.bark()

    print("\n--- 2. Multilevel Inheritance ---")
    electric_car = ElectricCar()
    electric_car.start()
    electric_car.drive()
    electric_car.charge()

    print("\n--- 3. Multiple Inheritance ---")
    phone = Smartphone()
    phone.take_photo()
    phone.play_music()

    print("\n--- 4. Hierarchical Inheritance ---")
    circle = Circle()
    rectangle = Rectangle()
    circle.describe()
    circle.draw()
    rectangle.describe()
    rectangle.draw()

    print("\n--- 5. Method Overriding ---")
    developer = Developer()
    developer.work()


if __name__ == "__main__":
    main()

