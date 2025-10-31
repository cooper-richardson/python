total = 0
count = 0

while True:
    number = int(input("Enter a number (-1 to finish): "))
    if number == -1:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)