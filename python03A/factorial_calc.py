number = int(input("Enter your number: "))
product = 1
for count in range(1, number + 1):
    product *= count
    #calculates the factorial
print(f"The factorial of {number} is {product}")