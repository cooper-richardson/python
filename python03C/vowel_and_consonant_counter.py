text = str(input("Enter text: "))
vowels = 0
consonants = 0

for char in text:
    if char in "aeiouAEIOU":
        vowels += 1
    elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants += 1

print(f"Vowels: {vowels}")
print(f"consonants: {consonants}")