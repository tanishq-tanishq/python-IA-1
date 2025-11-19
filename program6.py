# Program to read items from file and calculate bill details

items = {}        # dictionary to store item_name: (qty, price)
filename = "item.txt"

# Read file
with open(filename, "r") as f:
    for line in f:
        name, qty, price = line.split()
        items[name] = (int(qty), float(price))


total_items = 0
total_free = 0
amount = 0

for name, (qty, price) in items.items():
    total_items += qty

    # Free item: for every 3 items, 1 is free
    free = qty // 3
    total_free += free

    # Cost only for paid items
    amount += (qty - free) * price


# Apply 10% discount
discount = amount * 0.10
final_amount = amount - discount

# Output results
print("No. of items purchased:", total_items)
print("No. of free items:", total_free)
print("Amount to pay: ₹", amount)
print("Discount given: ₹", discount)
print("Final amount paid: ₹", final_amount)
