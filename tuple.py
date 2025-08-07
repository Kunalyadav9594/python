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