customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")

quantity = int(input("Enter quantity bought: "))
price = float(input("Enter price per unit: "))

amount = quantity * price
gst = amount * 5 / 100
final_total = amount + gst

print("Customer: " + customer_name)
print("Item: " + item_name)
print("Quantity: " + str(quantity))
print("Item Amount: ₹" + str(amount))
print("GST (5%): ruchi₹" + str(gst))
print("Final Total: ₹" + str(final_total))
