# Python string capitalize() method
txt = "hello, and welcome to my world"
x = txt.capitalize()
print(x)  # Output: "Hello, and welcome to my world"
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

# len() function
txt = "Hello, World!"
x = len(txt)
print(x)  # Output: 13
# The len() function returns the length of a string.(number of characters in the string)

# casefold() method
txt = "Hello, And Welcome To My World"
x = txt.casefold()
print(x)  # Output: "hello, and welcome to my world"
# The casefold() method returns a string where all characters are lower case. It is similar to the lower() 
# method but more aggressive in its conversion.

# center() method
txt = "Hello, World!"
x = txt.center(20)
print(x)  # Output: "     Hello, World!     "
# The center() method returns a string centered in a field of a given width. It pads the string with spaces 
# on both sides to achieve the desired width.

# parameterized center() method
txt = "Hello, World!"
x = txt.center(20, '*')
print(x)  # Output: "*****Hello, World!*****"
# The center() method can also take a second argument to specify a character to pad the string with.
# count() method
txt = "I love apples, apple pie, and apple juice"
x = txt.count("apple")
print(x)  # Output: 3
# The count() method returns the number of occurrences of a substring in the string.

txt = "I love apple, apple pie, apple juice"
x = txt.count("apple", 10, 30)
print(x)  # Output: 2
# The count() method can also take optional start and end parameters to limit the search to a specific range.

# encode() method
txt = "Hello, World!"
x = txt.encode()
print(x)  # Output: b'Hello, World!'
# The encode() method encodes the string into bytes using the default encoding (UTF-8).

# These examples uses ascii encoding, and a character that cannot be encoded, showing the result with different errors:
txt = "My name is Ståle"
print(txt.encode(encoding='ascii', errors='backslashreplace'))  # Output: b'My name is St\\xe5le'
print(txt.encode(encoding='ascii', errors='ignore'))  # Output: b'My name is Stle'
print(txt.encode(encoding='ascii', errors='replace'))  # Output: b'My name is St?le'
print(txt.encode(encoding='ascii', errors='xmlcharrefreplace')) 
 # Output: b'My name is St&#229;le'
# The encode() method can take an encoding type and an error handling scheme as parameters.

x = "Hello, welcome to my world"
x = txt.endswith(".")
print(x)  # Output: False
# The endswith() method checks if the string ends with a specified suffix and returns True or False.

# check if the string endswith the phrase "my world"
txt = "my world"
x = txt.endswith("my world")
print(x)  # Output: True
# The endswith() method can also take a start and end parameter to limit the search to a specific range.

# check if position 5 to 11 ends with "my world"
txt = "Hello, welcome to my world"
x = txt.endswith("my world", 5, 11)
print(x)  # Output: False
# The endswith() method can also take a start and end parameter to limit the search to a specific range.

# expandtabs() method
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)  # Output: "H  e  l  l  o"
# The expandtabs() method replaces all tab characters in the string with spaces. The number of spaces is determined 
# by the parameter passed to the method (default is 8).

# find() method
txt = "Hello, welcome to my world"
x = txt.find("welcome")
print(x)  # Output: 7
# The find() method returns the lowest index of the substring if found in the string. If not found, it returns -1.


