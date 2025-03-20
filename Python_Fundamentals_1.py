# Variables, Printing, Snakecase
current_year = 2025
print(current_year)

# To avoid change in variable value
CONSTANT_VARIABLES = 123
print(CONSTANT_VARIABLES)

# Numbers in Python
my_age = 36
PI = 3.14

# Order in which Python executes Mathematical Operations.(* / + -)
order_execution = 3*2/1+3-2
print(order_execution)

# Division result is always float
x = 8/3
print(x)

# Divide and remove value after decimal point
y = 8//3
print(y)

# Calculate reminder of two numbers using modulas
calculate_remainder = 5 % 2
print(calculate_remainder)

# Strings, Invert Quotes, Escaping, multiline strings/comments, f-string, string formatting, Adding Strings, Using str
my_name = "Michael"
print(my_name)

print("she's a girl")
print('That is a "common" noun')                # Invert Quotes

print("That is just \"freaking\" amazing")      # Escaping

greetings_everyone = f"My name is {my_name}"
print(greetings_everyone)                       # f-string

my_name = "Brian"

greetings_everyone = "My name is {}"
my_name = "Peter"
print(greetings_everyone.format(my_name))       # format string are basically used when we want to re-use a template.

x = """
         Hi 
      This is a
 Multi-line String/Comment                      
"""
print(x)                                        # multiline string/comment
                                                # f-string can be used in multi-line strings

blessed_name = "Ruel"
print("His Name is " + blessed_name)            # Adding Strings

blessed_age = 4
print("His Age is " + str(blessed_age))
