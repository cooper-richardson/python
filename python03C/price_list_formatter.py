item1 = str(input("Enter first item: "))
cost1 = float(input("Enter the first item's price: "))
item2 = str(input("Enter second item: "))
cost2 = float(input("Enter the second item's price: "))
item3 = str(input("Enter third item: "))
cost3 = float(input("Enter the third item's price: "))

tax1 = cost1 * .06
tax2 = cost2 * .06
tax3 = cost3 * .06

print(item1, "costs $", round(cost1, 2), "with tax $", round(tax1, 2))
print(item2, "costs $", round(cost2, 2), "with tax $", round(tax2, 2))
print(item3, "costs $", round(cost3, 2), "with tax $", round(tax3, 2))