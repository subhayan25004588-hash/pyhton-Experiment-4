# List Program

size = int(input("Enter the size of list: "))
items = []

for j in range(size):
    value = input("Enter an alphabet: ")
    items.append(value)

print("Given List:", items)

# Find Length
print("Total Elements:", len(items))

# Copy List
backup = items.copy()
print("Duplicate List:", backup)

# Add More Elements
items.extend(['m', 'n', 'o'])
print("List after adding elements:", items)

# Access Elements
print("Element at first position:", items[0])
print("Element at last position:", items[-1])

# Delete an Element
delete_value = input("Enter alphabet to delete: ")

if delete_value in items:
    items.remove(delete_value)

print("List after deletion:", items)

# Arrange List
items.sort()
print("List after sorting:", items)

# Change Order
items.reverse()
print("List after reversing:", items)

# Remove Last Element
items.pop()
print("List after removing last element:", items)
