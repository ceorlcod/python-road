# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Python can automatically detect the variable even without datatype (e.g. string, integer, float, or boolean)

# -----STRINGS-----

# for the string you need to put either "" or '' between the word you want to.
first_name = "Ceorl"
food = "pizza"
email = "example@fake.com"

print(first_name)

# formatted string "use f or F after the string put {} for the value you want to put"
print(f"Good Morning, {first_name}")
print(f"You like, {food}")
print(f"Your email is :, {email}")

# -----INTEGERS-----

# unlike string, you don't need "" or '' to have an integer instead, simply put the number to it.
age = 25
quantity = 3
number_of_students = 45

print(f"You are {age} years old")
print(f"You are buying {quantity} {food}")
print(f"Your class has {number_of_students} students")

# -----FLOATS-----

# similar to the integer, the float doesn't also need "" or '', but instead it needs to be in decimal
price = 10.99
gpa = 4.1

print(f"The price of {quantity} {food} is {price}")
print(f"{first_name}, your gpa is {gpa}")

# -----BOOLEANS-----

# unline the other variables, boolean have only 2 possible outcome which is the TRUE or FALSE
is_student = True
print(f"Are you student? {is_student}")

# you can use the boolean to check in the conditional statements like;

if is_student:
    print("You are student")
else:
    print("You are not student")


