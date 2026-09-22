import random

print("Random: ", random.random())
print("Random range: ", random.randrange(1,50))
print("Random int: ", random.randint(1,10))

num = [1,2,3,4,5]
print("Random Choice from arr: ", random.choice(num))

random.shuffle(num)
print("Random shuffle to arr: ", num)