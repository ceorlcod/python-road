# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Ceorl"
age = 20
gpa = 3.14
is_student = True

# To get the type or datatype of the variable you want, use the method of type()

type(name) # This is result into str
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# This will convert into integer instead of float
gpa = int(gpa)
print(gpa)

# This one will convert to float, so adding decimal to it
age = float(age)
print(age)

# It will print the true, so converting the value of the boolean into the string which is TRUE
name = bool(name)
print(name)

# This one will print 1 since the str has the value converted into 1, as long as it has value to it, it will convert into 1
name = int(name)
print(name)

# example of typecasting a str into integer but, str has no value to it
item = ""
item = int(item)
print(item)
