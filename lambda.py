# A lambda function is a small anonymous function.
# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments:
x = lambda a, b: a * b
print(x(5, 6))

# Summarize arguments a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

def my_function(n):
   return lambda a : a * n

mydoubler = my_function(2)
print(mydoubler(11))

# Or, use the same definition to make a function that always triples the number you send in:
def my_function(n):
   return lambda a : a * n
mytripler = my_function(3)
print(mytripler(11))

# Or, use the same function definition to make both functions, in the same program:
def my_function(n):
   return lambda a : a * n  
mydoubler = my_function(2)
mytripler = my_function(3)

print(mydoubler(11))
print(mytripler(11))

# Simple lambda for addition: A basic lambda assigned to a variable and called.
add = lambda x, y: x + y
print('Simple addition:', add(2, 3))

# Lambda with map() squares each number in a list. map() applies the lambda to every element.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print('squared numbers:', squared)