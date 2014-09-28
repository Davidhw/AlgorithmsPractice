import random

def swap(array,ind1,ind2):
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp
    return array

def createRandomList(size):
    return [random.randrange(1000) for x in range(size)]

def createRandomLists(numLists,multFactorDifference):
    randomListsOfSizeN = {}
    n = 1
    while n < multFactorDifference**numLists:
        randomListsOfSizeN[n] = createRandomList(n)
        n = n*multFactorDifference
    return randomListsOfSizeN

class Incrementor:
    def __init__(self):
        self.val = 0
    def inc(self):
        self.val+=1
    def getVal(self):
        return self.val

exampleArray = [9,2,2,4,-1,4,5,200,.5,3,0]
