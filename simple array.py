import array

# Create an array of integers
numbers = array.array('i', [1, 2, 3, 4, 5])

# Display the original array
print("Original array:", numbers)

# Append an element to the array
numbers.append(6)
print("After appending 6:", numbers)

# Insert an element at a specific position
numbers.insert(2, 10)
print("After inserting 10 at index 2:", numbers)

# Remove an element from the array
numbers.remove(4)
print("After removing 4:", numbers)

# Pop an element from the array
popped_element = numbers.pop()
print("After popping an element:", numbers)
print("Popped element:", popped_element)

# Access an element by index
print("Element at index 3:", numbers[3])

# Iterate over the array
print("Iterating over the array:")
for num in numbers:
    print(num)
