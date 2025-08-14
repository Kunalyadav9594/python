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

# Use the difference_update() to keep the items that are not present in both sets.
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set1.difference_update(set2)
print(set1)

# Symmetric Differences:
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Keep the items that are not present in both sets:
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1.symmetric_difference(set2)
print(set3)

# you can use the ^ operator instead of the symmetric_difference() method, and you will get the same result:
# Use ^ to join two sets:
set1={'apple','banana','cherry'}
set2={'google','microsoft','apple'}
set3=set1^set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it wil change the original set instead of returning a new set.
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1={'apple','google','cherry'}
set2={'banana', 'microsoft','apple'}
set1.symmetric_difference_update(set2)
print(set1)

# Set Methods
# Python has a set of built-in methods that you can use on sets.
# Add an element to the fruits set:
# add()
fruits={'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)

# Try to add an element that already exists.
fruits={'apple', 'banana', 'cherry'}
fruits.add('apple')
print(fruits)

# clear() method:
fruits={'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)

# copy() method.
fruits={'apple','banana', 'cherry'}
x=fruits.copy()
print(x)

# difference() method:
# Return a set that contains the items that only exist in set x, and not in set y:
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
z=x.difference(y)
print(z)

# Use - as a shortcut instead of difference():
a={'apple', 'banana', 'cherry'}
b={'google','microsoft','apple'}
my_set=a-b
print(my_set)

# Join more than two sets:
a={'apple','banana','cherry'}
b={'google','microsoft','apple'}
c={'cherry','microsoft','bluebird'}

my_set=a.difference(b,c)
print(my_set)

# Join more than two sets with the - operator:
a={'apple','banana','cherry'}
b={'google','microsoft','apple'}
c={'cherry','microsoft','bluebird'}

my_set=a-b-c
print(my_set)

# Reverse the example on the top of this page. Return a set that contains the items that only exist in set y,and not in set x:
x={'apple', 'banana', 'cherry'}
y={'google', 'microsoft', 'apple'}
z=y.difference(x)
print(z)

# difference_update()
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}
x.difference(y)
print(x)

# join more than two sets:
a={'apple','banana','cherry'}
b={'google','microsoft','apple'}
c={'cherry','micro','bluebird'}
a.difference_update(b,c)
print(a)

# Join more than two sets with the -= operator.
a={'apple','banana','cherry'}
b={'google','microsoft','apple'}
c={'cherry','micro','bluebird'}
a-=b|c
print(a)

# discard() Method:
fruits={'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)

