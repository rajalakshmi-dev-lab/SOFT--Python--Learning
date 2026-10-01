# Day 2: 30 Days of python programming

# Level 1

first_name = "Rajalakshmi"
last_name = "Santhosh"
full_name = "Rajalakshmi Santhosh"
country = "India"
city = "Kochi"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True

a, b, c = 10, 20, 30

# Level 2

# 1. Data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Length of first name
print(len(first_name))

# 3. Compare lengths
print(len(first_name))
print(len(last_name))

# 4. Numbers
num_one = 5
num_two = 4

# 5 - 11
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("total =", total)
print("diff =", diff)
print("product =", product)
print("division =", division)
print("remainder =", remainder)
print("exp =", exp)
print("floor_division =", floor_division)

# 12. Circle calculations
radius = 30
pi = 3.14

area_of_circle = pi * radius * radius
circum_of_circle = 2 * pi * radius

print("Area =", area_of_circle)
print("Circumference =", circum_of_circle)

# User input radius
radius = float(input("Enter radius: "))
area = pi * radius * radius
print("Area of circle =", area)

# 13. User input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = input("Enter age: ")

print(first_name)
print(last_name)
print(country)
print(age)

# 14. Python keywords
help('keywords')