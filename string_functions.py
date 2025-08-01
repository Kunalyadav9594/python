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