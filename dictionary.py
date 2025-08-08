# Create and print a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(type(thisdict))
# Output: <class 'dict'>

# Print the 'brand' value of the dictionary
print(thisdict["brand"])  # Accessing the value associated with the key 'brand'
# Output: Ford

# Duplicate keys are not allowed in dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020  # This will overwrite the previous 'year' key
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# Dictionary Length
print(len(thisdict))  # Returns the number of key-value pairs in the dictionary
# Output: 3
# Dictionary Items - Data Types
# Dictionary keys can be of any immutable data type (string, number, tuple)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "features": ["air conditioning", "navigation", "sunroof"]
}
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'features': ['air conditioning', 'navigation', 'sunroof']}
# The dict() Constructor
# You can create a dictionary using the dict() constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Accessing Dictionary Items
print(thisdict["model"])  # Accessing the value associated with the key 'model'
# Output: Mustang
# There are two ways to access dictionary items:
# 1. Using square brackets
print(thisdict["year"])  # Accessing the value associated with the key 'year'
# Output: 1964
# 2. Using the get() method
print(thisdict.get("brand"))  # Accessing the value associated with the key 'brand'
# Output: Ford
# The list of the keys is a view of the dictionary that any changes done to the dictionary will be reflected in the keys view
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.keys())  # Returns a view object that displays a list of all the keys in the dictionary
# Output: dict_keys(['brand', 'model', 'year'])
car["color"] = "red"  # Adding a new key-value pair
print(car.keys())
# Change the dictionary items
car["year"] = 2020  # Changing the value of an existing key
print(car)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'red'}
# Update the dictionary
car.update({"year": 2021, "color": "blue"})
print(car)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2021, 'color': 'blue'}

# Add dictionary items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"  # Adding a new key-value pair
print(thisdict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Removing Dictionary Items
# The pop() method removes the item with the specified key and returns its value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")  # Removes the item with key 'model'
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item (in Python 3.7 and later)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict) 
# Output: {'brand': 'Ford', 'model': 'Mustang'}

# The del keyword removes the item with the specified key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
# Output: {'brand': 'Ford', 'year': 1964}

# The del keyword can also delete the dictionary completely
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict  # Deletes the entire dictionary
# print(thisdict)  # This will raise a NameError since the dictionary no longer exists

# The clear() method empties the dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)  # Output: {}

# Print all key names in the dictionary, one by one:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
# Output: brand
# Output: model
# Output: year

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])  # Accessing the value using the key
# Output: Ford
# Output: Mustang
# Output: 1964
# Youcan also use the values() method to get all values in the dictionary
for x in thisdict.values():
    print(x)
# Output: Ford
# Output: Mustang
# Output: 1964
# You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
    print(x)
# Output: brand
# Output: model
# Output: year
# Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
    print(x, y)
# Output: brand Ford
# Output: model Mustang
# Output: year 1964
# Copy a Dictionary
# Make a copy of a dictionary with the copy() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Another way to make a copy is to use the dict() constructor
# Make a copy of a dictionary with the dict() function
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

