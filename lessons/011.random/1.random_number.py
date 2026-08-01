import random

low = 1
high = 100

# a random hole number
num = random.randint(low, high)
print(num)

# rand float number
num = random.random()
print(num)

# get a randon choice from a set
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

# shuffle to shuffle a seq
cards = ["2", "3", "4", "J", "Q"]
random.shuffle(cards)
print(cards)
