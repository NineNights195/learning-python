# if-else is a statements where you run some code only IF conditions is true and run other code ELSE when is false
# You can use 'elif' for continue IF statement from previously ELSE

age = int(input("Enter your age: "))

if age >= 18:
    print("You can enter night club")
elif age < 0:
    print("You have not born yet!")
else:
    print("You must be 18+ to enter night club")

# You can also use conditional expression (one-line if) 
response = input("Will you enter night club? (Y/n): ")
statement = True if response == "Y" else False
statement = response == "Y" # Or you can do this instead if variable is boolean
