#while condition:
i=0
while i <= 2:
    value = int(input("Guess a number:"))
    if value == 9:
        print("You guessed it correct")
        break
    i += 1
else:
    print("You failed")

