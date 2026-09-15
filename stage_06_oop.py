# Stage 6: Object Oriented Programming (OOP)

# Class and object
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Bruno", 3)
print(my_dog.bark())

# Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat()
print(cat.speak())

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print("Balance:", account.get_balance())

# Polymorphism
class Bird:
    def sound(self):
        return "Bird sound"

class Sparrow(Bird):
    def sound(self):
        return "Chirp"

class Duck(Bird):
    def sound(self):
        return "Quack"

for animal in [Sparrow(), Duck()]:
    print(animal.sound())
