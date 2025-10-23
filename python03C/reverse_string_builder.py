text = str(input("Enter a word: "))
text_rev = ""

for char in reversed(text):
    text_rev += char

print(text_rev)