# 1. Introduction to python
# What is Python? (High-level, interpreted, dynamically typed)
# Features of Python (Simple, portable, extensive libraries, etc.)

# 2. Python Indentation
# Python uses indentation instead of {} or ;
# Correct indentation is mandatory

# 3. Variables and Constants
# Variable → Name that stores data value
# No need to declare type explicitly
# Naming rules (letters, digits, underscore, no keywords)
# Constants → By convention written in uppercase
#   Example: PI = 3.14
#            GRAVITY = 9.8

# 4. Datatypes
# Numeric → int, float, complex
# Text → str
# Boolean → True / False
#   a = 5          # int
#   b = 3.14       # float
#   c = 2 + 3j     # complex
#   name = "Python" # str
#   is_active = True # bool

# 5.Typeconversion and casting
# 5a Implicit conversion
# x = 5      # int
# y = 2.5    # float
# result = x + y   # float (7.5)

# 5b Explicit conversion
# a = int("10")    # str → int
# b = float("3.5") # str → float
# c = str(100)     # int → str

# 6. Input and Output functions in Python
# print() → Output to the screen
# input() → Take input from the user
#   example1- print("Hello")
#   example2 - name="chandu"
#              age = 25
#               pritn("Name",name, "Age",age)
# The sep parameter
#     Defines how multiple values are separated.
#     print("Python", "Java", "C++", sep=", ")
# The end Parameter
#     Defines what to print at the end (default is newline \n).
#     print("Hello", end=" ")
#     print("World")

# 7. String formatting in print()
# 7a) Using f-strings
#     example: name="chandu"
#               age=25
#               print(f"My name is {name} and i am {age} years of age")
# 7b) Using .format()
#     example: print("My name is {} and i am {} years of age".format(name,age))
# 7c) Using % formatting (older style):
#     example: print("My name is %s and I am %d years old." % (name, age))

# 8. Input function in python
#   example: name = input("Enter your name: ")
#            print("Hello,", name)
#   To check datatype of value: type(name)
#   example: age = int(input("Enter your age: "))
#            height = float(input("Enter your height: "))
#            print(f"Age: {age}, Height: {height}")
#   Taking multiple inputs
#   Using split()-> a, b = input("Enter two numbers: ").split()
#                   print("First:", a, "Second:", b)
#   With type conversion:
#   a, b = map(int, input("Enter two numbers: ").split())
#   print("Sum =", a + b)




