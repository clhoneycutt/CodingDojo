import random

def randInt(min=0,max=100):
    randomNum = random.random() * max
    while randomNum < min:
        randomNum = random.random() * max
    return int(randomNum)
    
    