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

