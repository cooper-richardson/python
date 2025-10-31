import random
secret = random.randint(1, 50)
count = 0

while True:
    guess = int(input("Guess a number 1-50: "))
    count += 1
    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low")
    elif guess > 50:
        print("Not in the range!")
    elif guess == 0:
        print("Not in the range!")
    else:
        break

print (f"Congrats! You got it right in {count} tries")
    
    