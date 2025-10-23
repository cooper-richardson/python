lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
final = 0
for count in range(lower, upper + 1):
    final += count
print(f"The sum of numbers from {lower} to {upper} is {final}")