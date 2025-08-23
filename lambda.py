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