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

# format() method
txt = "For only {price:.2f} dollars!"
x = txt.format(price=49)
print(x)  # Output: "For only 49.00 dollars!"
# The format() method formats the specified value(s) and inserts them into the string. It can take multiple parameters 
# and format them according to the specified format.

# format() method with multiple parameters
txt1 = "My name is {fname}, I am {age} years old.".format(fname="Kunal", age= 23)
txt2 = "My name is {0}, I am {1} years old.".format("Kunal", 23)
print(txt1)  # Output: "My name is Kunal, I am 23 years old."
print(txt2)  # Output: "My name is Kunal, I am 23 years old."

# Formattaing types
# :<
txt = "We have {:<8} cows."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to specify the available space for the value.
#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))

# Use "b" to format the number as a binary number:
txt = "The number in binary is {:b}."
print(txt.format(5))  # Output: "The number in binary is 101."

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))
# Output: "We have 5 chickens."

# use "e" to format the number in scientific notation:
txt = "The number in scientific notation is {:e}."
print(txt.format(123456789))  # Output: "The number in scientific notation is 1.234568e+08"

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))

#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))




