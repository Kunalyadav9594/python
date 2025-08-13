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

# Remove 'banana' by using the discard() method.
this_set={'apple', 'banana', 'cherry'}
this_set.discard('banana')
print(this_set)

# Remove random item by using the pop() method:
this_set={'apple', 'banana', 'cherry'}
x=this_set.pop()
print(x)

# The clear() method empties the set:
this_set={'apple','banana','cherry'}
this_set.clear()
print(this_set)

# Loop items
this_set={'apple', 'banana','cherry'}
for x in this_set:
    print(x)

# Join sets:
# union() methods:
# Join set1 and set2 into a new  set:
set1={'a', 'b', 'c'}
set2={1,2,3}

set3=set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
# Use | to join two sets.
set1={'a', 'b', 'c'}
set2={1, 2, 3}

set3= set1 | set2
print(set3)

# Join multiple sets
# Join multiple set with the union() method:
set1={'a', 'b', 'c'}
set2={1, 2, 3}
set3={'John', 'Elena'}
set4={'apple', 'banana', 'cherry'}
my_set=set1.union(set2, set3, set4)
print(my_set)

# Use | to join two operators:
set1={'a','b','c'}
set2={1,2,3}
set3={'john','Elena'}
set4={'apple','banana','cherry'}

my_set=set1|set2|set3|set4
print(my_set)

# join a set with tuple
x={'a','b','c'}
y={1,2,3}

z=x.union(y)
print(z)

# update() method
# The update() method inserts the items in set2 into set1
set1={'a','b','c'}
set2={1,2,3}
set1.update(set2)
print(set1)

# Intersection
# Keep only the duplicates
# Join set1 and set2, but keep only the duplicates.
set1={'apple','banana','cherry'}
set2={1,2,'apple'}
set3=set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result:
# Use & to join two sets.
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1&set2
print(set3)

# The intersection_update method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set1.intersection_update(set2)
print(set1)

# Join sets that contains the value True,False,1 and 0, and see what is considered as duplicates.
set1={'apple',True,'banana',0,'cherry'}
set2={False,'google','apple',2,True}
set3=set1.intersection(set2)
print(set3)

# Difference
# Keep all items from set1 that are not in set2:
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1.difference(set2)
print(set3)

# You can use the - operator instead of difference() method, and you will get the same result.
set1={'apple','orange','banana'}
set2={'apple',1,2}
set3=set1-set2
print(set3)