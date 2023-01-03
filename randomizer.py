import time
from inspect import getframeinfo, stack

def getRandom(min, max):
    myRandom = getframeinfo(stack()[1][0]).lineno * int(str(time.time()).split('.')[1]) % (max - min)
    while True:
        if myRandom < min:
            myRandom = myRandom + max - min
        elif myRandom > max:
            myRandom = myRandom - max + min
        else:
            return myRandom

print(getRandom(-100, 100))
print(getRandom(-100, 100))
print(getRandom(-100, 100))


