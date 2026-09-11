Number = int(input("Enter a number: "))

# even or odd check
if Number % 2 == 0:
    even_or_odd ="The number is even."
else:
    even_or_odd = "The number is odd."

# positive, negative or zero check
if Number < 0:
    pos_neg_or_zero = "The number is negative."
elif Number == 0:
    pos_neg_or_zero = "The number is zero."
else:
    pos_neg_or_zero = "The number is positive."

print(even_or_odd)
print(pos_neg_or_zero)

