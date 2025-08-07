# Create tuple
thistuple=("apple", "banana", "cherry")
print(thistuple)
# Output: ('apple', 'banana', 'cherry')

# Since tuples are indexed , they can have items with the same value
thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'apple')

# Print the number of items in a tuple:
thistuple = ("apple", "banana", "cherry")
x = len(thistuple)
print(x)
# Output: 3

# create tuple with one item
thistuple = ("apple",)
print(type(thistuple))
# Output: <class 'tuple'>
# Note: A tuple with one item must have a comma after the item
thistuple = ("apple")
print(type(thistuple))
# Output: <class 'str'>  # This is a string, not a tuple

# Tuple items can be of any data type
# String, integer, float, boolean, etc.
thistuple1 = ("apple", "banana", "cherry")
thistuple2 = (1, 2, 3)
thistuple3 = (1.5, 2.5, 3.5)
thistuple4 = (True, False, True)
print(thistuple1)
print(thistuple2)
print(thistuple3)
print(thistuple4)
# Output:
# ('apple', 'banana', 'cherry')
# (1, 2, 3)
# (1.5, 2.5, 3.5)
# (True, False, True)

# Create a tuple with different data types
thistuple = ("apple", "banana", 1, 2, 3.5)
print(thistuple)
# Output: ('apple', 'banana', 1, 2, 3.5)
# Create a tuple with different data types
thistuple = ("apple", "banana", "cherry", 1, 2, 3.5, True)
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 1, 2, 3.5, True)

# Accessing tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # Accessing the second item
# Output: banana

# Negative indexing
print(thistuple[-1])  # Accessing the last item
# Output: cherry

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Accessing items from index 2 to 4
# Output: ('cherry', 'orange', 'kiwi')
# By leaving out the start index, the range starts from the beginning
print(thistuple[:4])  # Accessing items from the start to index 3
# Output: ('apple', 'banana', 'cherry', 'orange')
# By leaving out the end index, the range goes to the end of the tuple
print(thistuple[2:])  # Accessing items from index 2 to the end
# Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Change tuple values
# Tuples are immutable, so you cannot change their values directly.
# However, you can convert it to a list, change the value, and convert it back to a tuple.
x = ("apple", "banana", "cherry")
y = list(x)  # Convert tuple to list
y[1] = "orange"  # Change the second item
x = tuple(y)  # Convert list back to tuple
print(x)
# Output: ('apple', 'orange', 'cherry')

# Adding items to a tuple
# Tuples are immutable, so you cannot add items directly.
# However, you can concatenate tuples to create a new one.
thistuple1 = ("apple", "banana")
thistuple2 = ("cherry", "orange")
thistuple3 = thistuple1 + thistuple2
print(thistuple3)
# Output: ('apple', 'banana', 'cherry', 'orange')

# Add items
# Convert the tuple into a list, add 'orange', and convert it back to a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  # Convert tuple to list
y.append("orange")  # Add 'orange' to the list
thistuple = tuple(y)
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'orange')
# Add tuple to another tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y  # Concatenate the new tuple
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'orange')
# When creating a tuple with one item, remember to add a comma after the item, otherwise it will be treated as a string

# Removing items from a tuple
# Tuples are immutable, so you cannot remove items directly.
# However, you can convert it to a list, remove the item, and convert it back to a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")  # Remove 'banana' from the list
thistuple = tuple(y)  # Convert list back to tuple
print(thistuple)
# Output: ('apple', 'cherry')
