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


""" Getting User Input in Python:"""
# name = input("What is your name?: ")
# print(f"Hi {name} How are you doing?")

# age = int(input("What is your age?: "))
# print(f"You are {12 * age} months old")         # input always assumes type to be strings


# user_name = input("What is your name? :")
# print(f"Hello, {user_name}")

# user_age = int(input("What is your age? :"))
# age_in_months = user_age * 12
# print(f"{user_name} is {age_in_months} months old")

"""Booleans and Comparisions in Python:"""
my_name = "Mike"
are_you_mike = my_name == "Mike"
print(are_you_mike)

my_numbers = int(2)
validate_number = my_numbers >= 5
print(validate_number)


"""AND & OR in Python:"""
kid_name = "Ruel"
child_name = ""

null_list = []
value_list = [1,2,3]

null_int = 0
value_int = 1

print(bool(value_int))

age_input = 18
validate_eligible = int(age_input) >= int(18) and int(age_input) <= int(65)
print(validate_eligible)

select_fruit = "jackfruit"
validate_fruit = select_fruit == "apple" or select_fruit == "mango"
print(validate_fruit)

"""Lists in Python: """
my_numbers = [9, 12, 1988]
print(my_numbers)
print(my_numbers[1])

date_of_birth = [
    ["Ruthushree", 21121990],
    ["Ruel", 18032021],
    ["Michael", 9121988]
]
print(date_of_birth[2][1])

date_of_birth.append(["Samson", 19111962])
print(date_of_birth)

date_of_birth.remove(["Ruel", 18032021])
print(date_of_birth)

date_of_birth.remove(date_of_birth[1])
print(date_of_birth)

"""Tuples in Python:"""
my_tuple = ("st paul's", "RLS", "SCTIT")
#print(my_tuple.append("Envestnet"))
print(my_tuple + ("Envestnet",))


"""Sets in Python:"""

"""Dictionaries in Python:"""

"""Length and sum:"""

"""Joining a List:"""