Mathematics = int(input("Enter marks for Mathematics: "))
Physics = int(input("Enter marks for Physics: "))
Chemistry = int(input("Enter marks for Chemistry: "))
English = int(input("Enter marks for English: "))

Total_marks = Mathematics + Physics + Chemistry + English
Average_marks = Total_marks / 4

print("Mathematics: ", Mathematics)
print("Physics: ", Physics)
print("Chemistry: ", Chemistry)
print("English: ", English)

print("Total Marks: ", Total_marks)
print("Average Marks: ", round(Average_marks, 2))


