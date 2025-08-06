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

# copying a list
fruits = ["apple", "banana", "cherry"]
newlist = fruits.copy()
print(newlist)
# Output: ['apple', 'banana', 'cherry']

# counting items in a list
fruits = ["apple", "banana", "cherry"]
x= fruits.count("apple")
print(x)
# Output: 1

# Return the number of items the value 9 appears in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
x = numbers.count(9)
print(x)
# Output: 2

# extending a list
fruits = ["apple", "banana", "cherry"]
cars = ["ford", "bmw", "volvo"]
fruits.extend(cars)
print(fruits)
# Output: ['apple', 'banana', 'cherry', 'ford', 'bmw', 'volvo']

# indexing a list
fruits = ["apple", "banana", "cherry"]
x= fruits.index("banana")  # Returns the index of the first occurrence of "banana"
print(x)
# Output: 1

# what is the position of value 32:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 32]
x = numbers.index(32)  # Returns the index of the first occurrence of 32
print(x)

# find the position of 'cherry' ,but start the search at position 4:
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "cherry"]
x = fruits.index("cherry", 4)   # Returns the index of "cherry" starting from index 4
print(x)

# inserting into a list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")  # Inserts "orange" at index 1
print(fruits)
# Output: ['apple', 'orange', 'banana', 'cherry']

# pop an item from a list
fruits = ["apple", "banana", "cherry"]
x = fruits.pop(1)
print(x)  # Removes and returns the item at index 1
# Output: banana
print(fruits)  # Remaining items in the list
# Output: ['apple', 'cherry']
fruits.pop()  # Removes and returns the last item in the list
print(fruits)
# Output: ['apple'] 

# pop() method
# Remove the "banana" element of the fruit list.
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)  # Removes the item at index 1
print(fruits)
# Output: ['apple', 'cherry']

# sort the list reverse
cars = ["Ford", "BMW", "Volvo"]
cars.sort(reverse=True)  # Sorts the list in descending order
print(cars)
# Output: ['Volvo', 'Ford', 'BMW']

# A function that returns the length of the value of the list
def myFunc(e):
    return len(e)

cars =["Ford", "Mitsubishi", "BMW", "Volvo"]
cars.sort(key=myFunc)  # Sorts the list based on the length of each string
print(cars)
# Output: ['BMW', 'Ford', 'Volvo', 'Mitsubishi']

# Sort a list os dictionaries on the 'year' value of the dictionaries:
# A function tjat returns the 'year' value:
def myFunc(e):
    return e['year']
cars = [
    {'car' : 'ford', 'year' : 2005},
    {'car':"mitsubishi", 'year': 2000},
    {'car':"bmw", 'year': 2010},
    {'car':"volvo", 'year': 2015}
]
cars.sort(key=myFunc)  # Sorts the list of dictionaries by the 'year' key
print(cars)
# Output: [{'car': 'mitsubishi', 'year': 2000}, {'car': 'ford', 'year': 2005}, {'car': 'bmw', 'year': 2010}, {'car': 'volvo', 'year': 2015}]

#  sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)
cars = ["Ford", "Mitsubishi", "BMW", "Volvo"]
cars.sort(key=myFunc, reverse=True)  # Sorts the list based on the length of each string in descending order
print(cars)
# Output: ['Mitsubishi', 'Volvo', 'Ford', 'BMW']
