Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
University = input("Enter your university name: ")
Semester = int(input("Enter your semester (1-8): "))
Cgpa = float(input("Enter your CGPA (0.0 - 4.0): "))
Programming_experience = input("Do you have programming experience? (yes/no): ")
Interest_in_AI = input("Are you interested in AI? (yes/no): ")

#Age check
if Age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Academic status check
if Cgpa >= 3.5:
    academic_status = "Excellent"
elif Cgpa >= 3.0:
    academic_status = "Good"
elif Cgpa >= 2.5:
    academic_status = "Satisfactory"
else:
    academic_status = "Needs Improvement"

# Program eligibility check
if Age >= 18 and Semester >= 3 and Cgpa >= 3.2 and Programming_experience.lower() == "yes" and Interest_in_AI.lower() == "yes":
    eligibility = "Eligible for AI program"
else:
    eligibility = "Not eligible for AI program"   

print("\n========== Mini Profile Checker ==========")
print("Name: ", Name)
print("Age: ", Age)
print("University: ", University)
print("Semester: ", Semester)
print("CGPA: ", Cgpa)
print("Age Status: ", status)
print("Academic Status: ", academic_status)
print("Ai Program Eligibility: ", eligibility)