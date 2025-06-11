# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = input("What is your age?: ")

# You can't add to it, since input() only return the value as STRING
# To be able to add, you need to use the typecast methods
age = int(age)
age = age + 1

print(f"Hello, {name}")
print(f"You are {age} years old")

# You can also just put the type cast method before the input()
price = float(input("How much is the price you want?: "))

print(f"the price is {price}")