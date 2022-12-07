import random
from time import sleep

space = {'A': 'clean', 'B': 'clean'}

def makeDirty():
    randlist = random.choice(list(space.keys()))
    space[randlist] = 'dirty'
    print(randlist)
    print(space)


while True:
    makeDirty()
    if space['A'] == 'clean' and space['B'] == 'clean':
        sleep(3)
        continue

    elif space['A'] == 'clean' and space['B'] == 'dirty':
        space['B'] = 'clean'
        sleep(3)
        print("moving to B")
        

    elif space['A'] == 'dirty' and space['B'] == 'clean':
        space['A'] = 'clean'
        sleep(3)
        print("moving to A")
        

    elif space['A'] == 'dirty' and space['B'] == 'dirty':
        sleep(3)
        continue
