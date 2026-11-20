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
