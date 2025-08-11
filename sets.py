# Create a set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Output: {'apple', 'banana', 'cherry'}

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Output: {'apple', 'banana', 'cherry'}

# True and 1 are considered the same:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 are considered the same:
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)
# Output: {'apple', 'banana', 'cherry', 2, False}

# Get the length of a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Output: 3

# Set items can be of any data type:
thisset = {"apple", "banana", "cherry", 1, 2, 3}
print(thisset)
# Output: {'apple', 'banana', 'cherry', 1, 2, 3}

# type() can be used to check the type of a set:
thisset = {"apple", "banana", "cherry"}
print(type(thisset))
# Output: <class 'set'>

# Access set items
# Loop through the set, and print the values:
thisset={"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Check if "banana" is present in the set:
thisset={"apple", "banana", "cherry"}
print("banana" in thisset)

# Check if "banana" is NOT present in the set
thisset={"apple","banana", "cherry"}
print("banana" not in thisset)