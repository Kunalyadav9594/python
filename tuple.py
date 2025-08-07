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
# Deleting a tuple
thistuple = ("apple", "banana", "cherry")
del thistuple  # Deletes the entire tuple
# print(thistuple) 
 # This will raise an error because thistuple is deleted

# Finding items in a tuple
thistuple = ("apple", "banana", "cherry")
x = thistuple.index("banana")  # Returns the index of the first occurrence of "banana"
print(x)
# Output: 1

# Unpacking a tuple
thistuple = ("apple", "banana", "cherry")
(a, b, c) = thistuple
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry

fruits = ("apple", "banana", "orange")
(green, yellow, orange) = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(orange) # Output: orange

# Using an asterisk to unpack
thistuple = ("apple", "banana", "cherry", "orange")
(a, *b) = thistuple
print(a)  # Output: apple
print(b)  # Output: ['banana', 'cherry', 'orange']
print(type(b))  # Output: <class 'list'>  # b is a list

# Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for fruit in thistuple:
    print(fruit)
    print(type(fruit))  # Output: <class 'str'>  # Each fruit is a string

# Loop through the index numbers
# You can also loop through the tuple items by referring to their index numbers
# Use the range() and len() functions to create a suitable iterable
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
    print(type(thistuple[i]))
# Output:
# apple
# <class 'str'>
# banana
# <class 'str'>
# cherry
# <class 'str'>

# Using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
# Output:
# apple
# banana
# cherry
# 
# Multiply tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator
# This example creates a new tuple with the content of the original tuple repeated 2 times
thistuple = ("apple", "banana", "cherry")
mytuple = thistuple * 2
print(mytuple)
# Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# Output: ('a', 'b', 'c', 1, 2, 3)    

# Tuple() methods
# count() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)  # Returns the number of times 5 appears in the tuple
print(x)
# Output: 2
# index() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(7)
print(x)  # Returns the index of the first occurrence of 7
# Output: 2
# index() method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x =thistuple.index(8)
print(x)  # Returns the index of the first occurrence of 8
# Output: 3