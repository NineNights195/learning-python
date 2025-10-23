# input() is a function to tell user to enter data. Always be string

input("Enter your favorite thing: ")
name = input("Enter your Name: ")   # You can collect data to variable
print(f"Hello {name}.")
gpa = float(input("Enter your lasted GPAs: "))  # You can also timecasing at the same time
gpa += 0.5
print(f"Luckly, teacher increase your GPAs to {gpa}!")
