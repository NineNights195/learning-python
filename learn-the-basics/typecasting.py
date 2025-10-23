# Typecasting is the process of converting a variable from one data type to another
# Important for user input

name = "Thanarat"
age = 17
gpa = 3.6

age = str(age)  # str() convert to string
age += "25"     # When plus string to string, it will put them to the back
print(age)

gpa = int(gpa)  # int() convert to integer
print(gpa)      # Always round down

age = float(age)    # float() convert to float
print(type(age))    # Tips: to print type of variable, use type()

name = bool(name)   # bool() convert to boolean
# Always return true unless it's empty
# Example case
if name:
    print("Name entered")
else:
    print("Please insert your name")
