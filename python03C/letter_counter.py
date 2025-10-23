text = str(input("Enter text: "))
amount = 0

for char in text:
    if char in "a":
        amount += 1

print(f"Amount of lowercase a: {amount}")