weight = int(input("Enter weight of your package: "))
cost = 0

# Ground shipping
if weight <= 2:
    cost = 1.50
elif weight <= 6:
    cost = 3.00
elif weight <= 10:
    cost = 4.00
else:
    cost = 4.75
cost = weight * cost + 20
print("Ground Shipping $", cost)

# Ground shipping premium
cost = weight * cost + 125
print("Ground Shipping Premium $", cost)

# Drone shipping
if weight <= 2:
    cost = 5.50
elif weight <= 6:
    cost = 9.00
elif weight <= 10:
    cost = 12.00
else:
    cost = 14.25
cost = weight * cost
print("Drone Shipping $", cost)

