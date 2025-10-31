total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    total_sum += number
    if number == 0:
        print(f"Total sum: {total_sum}")
    