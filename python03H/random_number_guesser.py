import random
guesses = 0
print("Think of a number between 1 and 100...")
guess = random.randint(1, 100)
while True:
    answer = input(f"My guess is {guess}. (Higher/Lower/Correct): ")
    if answer == "Higher":
        guess = random.randint(guess, 100)
        guesses += 1
    elif answer == "Lower":
        guess = random.randint(1, guess)
        guesses += 1
    elif answer == "Correct":
        guesses += 1
        break
    else:
        print("Invalid answer")
if guess == 1:
    print(f"I got it in {guesses} guess!")
else:
    print(f"I got it in {guesses} guesses!")