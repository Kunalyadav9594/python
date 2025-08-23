# Creating a function.
def my_function():
    print("Hello from a function")

# Calling a function.
my_function()

# Arguments - Information can be passed into functions as arguments.
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of arguments - A function can have one or more arguments.
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

# Arbitrary arguments, *args - If you do not know how many arguments that will be passed into your function, add a * before the parameter name.
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Keyword arguments - You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitary keyword arguments, **kwargs - If you do not know how many keyword arguments that will be passed into your function, add two asterisks: ** before the parameter name.
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

# Default parameter value - If we call the function without argument, it uses the default value.
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()  # Will use the default value "Norway"
my_function("Brazil")

# Passing a list as an argument - You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return values - To let a function return a value, use the return statement.
def my_function(x):
    return 5 * x    
print(my_function(3))

# The pass Statement
def my_function():
    pass  # Used when a function is required syntactically but you do not want any code to be executed.

# Positional - only arguments
def my_function(x, /):
    print(x)
my_function(3)  # Valid

# Without the , / you rae actually allowed to use keyword arguments even if the  function expects positional arguments.
def my_function(x):
    print(x)
my_function(x=3)  # Valid

# But when adding the ,/ you will get an error if you try to send a keyword argument:
def my_function(x, /):
    print(x)
# my_function(x=3)  # Invalid - will raise a TypeError
# TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'x'

# Keyword - only arguments
def my_function(*, x):
    print(x)    
my_function(x=3)  # Valid
# my_function(3)  # Invalid - will raise a TypeError

# Without the *, you are actually allowed to use positional arguments even if the function expects keyword arguments.
def my_function(x):
    print(x)
my_function(3)  # Valid

# Combine Positional - only and Keyword - only arguments
# You can combine the two argument types in the same function:
# Any argument before the / must be positional only.
def my_function(a, b, /, *,c,d):
    print(a+b+c+d)
my_function(5,6,c=7,d=8)  # Valid

# Recursion - The function calls itself.
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\nRecursion Example Results :")
tri_recursion(6)

