low = 0
high = 100
correct = int(input("Pick a number between 1 and 100 (inclusive) "))
guess = ""
num = (low + high) / 2 

while (guess != "C"):
    print(f"My guess is: {num}")
    guess = input("Is my guess too low (L), too high (H), or correct (C)?\n")
    if guess == 'C':
        break
    elif guess == 'L':
        low = num
    elif guess == 'H':
        high = num
    num = (low + high) / 2