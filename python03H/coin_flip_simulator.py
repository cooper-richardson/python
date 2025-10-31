import random
headscount = 0
tailscount = 0
print("Flipping a coin 20 times...")
for count in range(20):
    result = random.randint(0, 1)
    if result == 0:
        print("T", end=" ")
        tailscount += 1
    else:
        print("H", end=" ")
        headscount += 1
print(" ")
print(f"Heads: {headscount}")
print(f"Tails: {tailscount}")