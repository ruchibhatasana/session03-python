customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")

quantity = int(input("Enter quantity bought: "))
price = float(input("Enter price per unit: "))

amount = quantity * price
gst = amount * 5 / 100
final_total = amount + gst

print("\n\t\"Ruchi Kirana Store\"")
print("\t----------------------------")

print("Customer:\t" + customer_name)
print("Item:\t\t" + item_name)
print("Quantity:\t" + str(quantity) + "\n")

print("Item Amount:\t₹" + str(amount))
print("GST (5%):\t₹" + str(gst))
print("Final Total:\t₹" + str(final_total))
print("Whole Rupees:\t₹" + str(int(final_total)))


# TEST CASE 1
# Customer: Ruchi
# Item: Rice
# Quantity: 4
# Item Amount: ₹182.0
# GST (5%): ₹9.1
# Final Total: ₹191.1
# Whole Rupees: ₹191


# TEST CASE 2
# Customer: Ruchi
# Item: Wheat
# Quantity: 2
# Item Amount: ₹300.0
# GST (5%): ₹15.0
# Final Total: ₹315.0
# Whole Rupees: ₹315
