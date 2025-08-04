thislist = ["apple", "banana", "cherry"]
print(thislist)
# Output: ['apple', 'banana', 'cherry']

# list methods
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds an item to the end of the list
print(fruits)
# Output: ['apple', 'banana', 'cherry', 'orange']

a = ["apple", "banana", "cherry"]
b = ["ford", "bmw", "volvo"]
a.append(b)  # Appends the list b to the end of list a
print(a)
# Output: ['apple', 'banana', 'cherry', ['ford', 'bmw', 'volvo']]

# clearing a list
fruits = ["apple", "banana", "cherry"]
fruits.clear()  # Removes all items from the list
print(fruits)