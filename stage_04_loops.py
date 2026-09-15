# Stage 4: For/While Loops

# For loop
print("For loop example:")
for i in range(1, 6):
    print(i)

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
print("While loop example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Break and continue
print("Break/Continue example:")
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)
