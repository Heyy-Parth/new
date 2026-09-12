# Polymorphism example

class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Duck(Bird):
    def sound(self):
        print("Quack")

for animal in [Sparrow(), Duck()]:
    animal.sound()
