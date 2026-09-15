# Stage 3: Data Structures

# List
numbers = [1, 2, 3, 4]
print("List:", numbers)
print("First element:", numbers[0])
numbers.append(5)
print("After append:", numbers)

# Tuple
point = (10, 20)
print("Tuple:", point)
print("Tuple first element:", point[0])

# Set
unique_numbers = {1, 2, 2, 3, 4}
print("Set:", unique_numbers)
unique_numbers.add(5)
print("Set after add:", unique_numbers)

# Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Dictionary:", student)
print("Student name:", student["name"])
student["city"] = "New York"
print("Updated dictionary:", student)

# String
message = "Hello, Python!"
print("String:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Split:", message.split(","))
