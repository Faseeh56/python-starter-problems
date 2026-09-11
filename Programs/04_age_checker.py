Age = int(input("Enter your age: "))

if Age >= 0 and Age <= 12:
    print("You are a child.")
elif Age >= 13 and Age <= 17:
    print("You are a teenager.")
elif Age >= 18 and Age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


print("Thank you for using the age checker program!")