import random

def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

# Main program
total = 0

for _ in range(100):
    total += randDice()

average = total / 100
average = round(average, 2)

print("Average of 100 rolls:", average)
