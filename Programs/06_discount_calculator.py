Purchase_amount = float(input("Enter the purchase amount: "))

if Purchase_amount < 0:
    print("Invalid purchase amount. Please enter a positive value.")
elif Purchase_amount < 5000:
    discount = 0
    final_amount = Purchase_amount
elif Purchase_amount >= 5000 and Purchase_amount < 10000:
    discount = 0.10 * Purchase_amount
    final_amount = Purchase_amount - discount
elif Purchase_amount >= 10000 and Purchase_amount < 20000:
    discount = 0.15 * Purchase_amount
    final_amount = Purchase_amount - discount
else:
    discount = 0.20 * Purchase_amount
    final_amount = Purchase_amount - discount

print("Purchase Amount: ", Purchase_amount)
print("Discount: ", discount)
print("Discounted Amount: ", Purchase_amount - discount)
print("Final Amount to be paid: ", final_amount)