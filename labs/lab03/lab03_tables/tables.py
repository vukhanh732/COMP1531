from random import randint

num1 = randint(2, 12)
num2 = randint(2, 12)
answer = num1 * num2

while True:
    guess = int(input(f"What is {num1} x {num2}? "))
    if guess == answer:
        print("Correct!")
        break
    else:
        print("Incorrect - try again.")