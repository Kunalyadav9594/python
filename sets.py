# Create a set:
set = {"apple", "banana", "cherry"}
print(set)
# Output: {'apple', 'banana', 'cherry'}

# Duplicate values will be ignored:
set = {"apple", "banana", "cherry", "apple"}
print(set)
# Output: {'apple', 'banana', 'cherry'}

# True and 1 are considered the same:
set = {"apple", "banana", "cherry", True, 1, 2}
print(set)

# False and 0 are considered the same:
set = {"apple", "banana", "cherry", False, 0, 2}
print(set)
# Output: {'apple', 'banana', 'cherry', 2, False}

# Get the length of a set:
set = {"apple", "banana", "cherry"}
print(len(set))
# Output: 3

# Set items can be of any data type:
set = {"apple", "banana", "cherry", 1, 2, 3}
print(set)
# Output: {'apple', 'banana', 'cherry', 1, 2, 3}

# type() can be used to check the type of a set:
set = {"apple", "banana", "cherry"}
print(type(set))
# Output: <class 'set'>

# Access set items
# Loop through the set, and print the values:
set={"apple", "banana", "cherry"}

for x in set:
    print(x)

# Check if "banana" is present in the set:
set={"apple", "banana", "cherry"}
print("banana" in set)

# Check if "banana" is NOT present in the set
set={"apple","banana", "cherry"}
print("banana" not in set)

# Add set items
# Add an item to a set, using the add() method.
set={'apple','banana','cherry'}
set.add('orange')
print(set)

# update() method:
# Add elements from tropical into this_set :
this_set={'apple', 'banana', 'cherry'}
tropical={'pineapple', 'mango', 'papaya'}

this_set.update(tropical)
print(this_set)

# Remove set items
this_set={'apple', 'banana', 'cherry'}
this_set.remove('banana')
print(this_set)

# Add any element of a list to at set:
this_set={'apple', 'banana', 'cherry'}
my_list=['kiwi', 'orange']
this_set.update(my_list)
print(this_set)

# Remove set items
# Remove 'banana' by using the remove() method.
this_set={'apple','banana','cherry'}
this_set.remove('banana')
print(this_set)
