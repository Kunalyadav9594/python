# Get the value of the first array item.
cars = ["Ford", "Volvo", "BMW"]
x = cars[1]
print(x)

# Modify the value of the first array item.
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"

# The length of an array can be found with the len() function.
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# Looping through an array.
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# Adding an array item using the append() method.
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

# Removing an array item using the remove() method.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

# Removing an array item using the pop() method.
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

# Array methods()
# append()	-	Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

# Add list to the list
fruits = ['apple', 'banana', 'cherry']
more_fruits = ['orange', 'mango', 'grapes']
fruits.extend(more_fruits)
print(fruits)

# clear()	-	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)

# copy()	-	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
x = fruits.copy()
print(x)