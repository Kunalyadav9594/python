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