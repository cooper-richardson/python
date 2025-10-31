import random
numbers = []
for count in range(6):
    num = random.randint(1, 49)
    if num not in numbers:
        numbers.append(num)
print("Your lottery numbers are: ", numbers)