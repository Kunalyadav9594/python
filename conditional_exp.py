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

# You can also have an else statement without an elif statement.
a = 200 
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# one line if statement
a = 200
b = 33
if a > b: print("a is greater than b")

# one line if else statement
a=2 
b=330
print("A") if a > b else print("B")

# You can also have multiple else statements on the single line.
a=330   
b=330
print("A") if a > b else print("=") if a == b else print("B")

# And - The and keyword is a logical operator, and is used to combine conditional statements.
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or - The or keyword is a logical operator, and is used to combine conditional statements.
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True") 
