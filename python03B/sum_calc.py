start = int(input("Enter the starting amount: "))
end = int(input("Enter the ending amount: "))
sum = 0
for count in range(start, end + 1):
    sum = sum + count
print(f"The sum of numbers {start} to {end} is {sum}")