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

