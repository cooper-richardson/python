number = int(input("How many numbers to process?: "))
current = 0
loop = 1
for count in range(1, number + 1):
    new_num = int(input(f"Enter number {loop}: "))
    loop += 1
    current += new_num
current = current / number
print(f"The average is {current}")