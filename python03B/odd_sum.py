num = int(input("Enter a number: "))
final = 0
for count in range(1, num + 1, 2):
    final += count
    print(final)
print(f"The sum of odd numbers from 1 to {num} is {final}")