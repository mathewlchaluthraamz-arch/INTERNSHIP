# Create a list of 5 numbers
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Append (add element at the end)
numbers.append(60)
print("After append:", numbers)

# Index (find position of an element)
pos = numbers.index(30)
print("Index of 30:", pos)

# Remove (remove a specific element)
numbers.remove(20)
print("After remove:", numbers)

# Pop (remove last element)
removed_item = numbers.pop()
print("After pop:", numbers)
print("Popped element:", removed_item)

# Insert (add element at a specific position)
numbers.insert(2, 25)
print("After insert:", numbers)

# Length (number of elements in list)
length = len(numbers)
print("Length of list:", length)