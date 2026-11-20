customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")

quantity = int(input("Enter quantity bought: "))
price = float(input("Enter price per unit: "))

total = quantity * price

print("Customer:", customer_name, "| Item:", item_name, "| Quantity:", quantity)
print("Total Bill: ₹", total)
