Number = int(input("Enter a number: "))

if Number % 2 == 0:
    even_or_odd ="The number is even."
else:
    even_or_odd = "The number is odd."

if Number < 0:
    pos_neg_or_zero = "The number is negative."
elif Number == 0:
    pos_neg_or_zero = "The number is zero."
else:
    pos_neg_or_zero = "The number is positive."

print(even_or_odd)
print(pos_neg_or_zero)

