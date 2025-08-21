# Python If...Else Conditional Statements
# if statements are used to execute a block of code based on a condition.
a=33
b=200
if b > a:
    print("b is greater than a")
# In this example we used two variables, a and b, which are used as the part of the if statement to check whether b is greater than a.
# If the condition evaluates to True, the code block inside the if statement is executed.
# If the condition evaluates to False, the code block inside the if statement is skipped.

# Indentation is important in Python. The code block inside the if statement must be indented.
# If the code block is not indented, Python will raise an IndentationError.
# If statement without indentation raises an error

# elif - The elif keyword is python's way of saying 'if the previous conditions were not true, then try this condition'.

a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else - The else keyword is python's way of saying 'if the previous conditions were not true, then do this'.
a=200
b=33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")    
else:
    print("a is greater than b")    