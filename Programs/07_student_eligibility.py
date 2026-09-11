Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Semester = int(input("Enter your semester (1-8): "))
CGPA = float(input("Enter your CGPA (0.0 - 4.0): "))

if Age >= 18 and Semester >= 3 and CGPA >= 3.2:
    eligibility = f"Congratulations! {Name}, \nYou are eligible for the AI engineering program."
else:
    eligibility = f"Sorry, {Name}, \nYou are not eligible for the AI engineering program."

print(eligibility)