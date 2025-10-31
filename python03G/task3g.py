password = "python123"

while True:
    guess = str(input("Enter Password: "))
    if guess != password:
        print("Wrong password. Try again")
    if guess == password:
        print("Access granted!")
        break
