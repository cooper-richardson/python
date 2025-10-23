name = str(input("What is your name?: "))
repeat = int(input("How many times to repeat?: "))
for count in range(repeat):
    print(name, end=" ")
    #repeats entered name for the entered amount of time