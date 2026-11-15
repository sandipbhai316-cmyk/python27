

# # Integer variable
# age = 25
# print("Age:", age)


# # Float variable
# height = 5.9
# print("Height:", height)

# # String variable
# name = "John"
# print("Name:", name)
# print(type(name))  # Output: <class 'str'>

# # Boolean variable
# is_student = True
# print("Is Student:", is_student)

# # List variable
# fruits = ["apple", "banana", "cherry"]
# print("Fruits:", fruits)


# # Dictionary variable
# person = {"name": "Alice", "age": 30, "city": "New York"}
# print("Person:", person)
# print("Type of person is:",type(person))  # Output: <class 'dict'>


# #identity operator
# x = 10
# y = 10
# print(x is y)  # Output: True

# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is y)  # Output: False

# x = [1, 2, 3]
# y = x
# print(x is y)  # Output: True


# #Membership operator
# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)  # Output: True
# print("grape" not in fruits)  # Output: True    


# #Ternary operator
# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print("Status:", status)  # Output: Adult

# #input output
# name = input("Enter your name: ")
# print("Hello, " + name + "!")       

# value = int(input("Enter a number: "))
# print("You entered:", value)

# # Taking input from the user
# name = input("Enter your name: ")
# print("Hello, " + name + "!")  # Output the name

# # Taking an integer input
# age = int(input("Enter your age: "))
# print("You are", age, "years old.")  # Output the age

# # Taking a float input
# height = float(input("Enter your height in meters: "))
# print("Your height is", height, "meters.")  # Output the height

# # Taking multiple inputs
# city, country = input("Enter your city and country (separated by a space): ").split()
# print("You live in", city, "in", country + ".")  # Output the city and country

# Integer to float
num = 10
num_float = float(num)
print("Integer to Float:", num_float, "| Type:", type(num_float))

# Float to integer
height = 5.9
height_int = int(height)
print("Float to Integer:", height_int, "| Type:", type(height_int))

# String to integer
num_str = "123"
num_int = int(num_str)
print("String to Integer:", num_int, "| Type:", type(num_int))

# String to float
num_str = "123.45"
num_float = float(num_str)
print("String to Float:", num_float, "| Type:", type(num_float))

# Integer to string
age = 25
age_str = str(age)
print("Integer to String:", age_str, "| Type:", type(age_str))

# Float to string
pi = 3.14159
pi_str = str(pi)
print("Float to String:", pi_str, "| Type:", type(pi_str))