import random
wins = 0
losses = 0
current = random.randint(1, 100)
for count in range(2):
    print(f"Current number: {current}")
    num = random.randint(1, 100)
    guess = input("Will the next number be (h)igher or (l)ower? ")
    print(f"Next number: {num}")
    if guess == "h" and num > current:
        wins += 1
        print("You win")
    elif guess == "l" and num < current:
        wins += 1
        print("You win")
    else:
        losses += 1
        print("You lose")
print(f"Score: {wins} win/s, {losses} loss/es")