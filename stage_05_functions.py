# Stage 5: Functions

# Basic function
def greet():
    print("Hello, world!")


greet()

# Function with parameters

def add(a, b):
    return a + b

print("Sum:", add(3, 4))
print("Sum2:", add(10, 20))

# Default arguments

def welcome(name="Guest"):
    return f"Welcome, {name}!"

print(welcome())
print(welcome("Alice"))

# Lambda function
square = lambda x: x * x
print("Square:", square(6))

numbers = [1, 2, 3, 4]
print("Doubled:", list(map(lambda n: n * 2, numbers)))
