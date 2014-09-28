import random, commonFunctions
from doubleLinkedList import doubleLinkedList as linkedList

# inputed into the hashtable
numberOfNumbers = 10000 
# size of hash table
arraySize = 100000 
# random numbers have values 0-maxNumber
maxNumber = 2*10**9 
#maxNumber = 1000

def getRand():
    return random.randint(0,maxNumber)

class Hash():
    def __init__(self,size):
        self.array = [None for _ in range(size)]
        # if the size is a multiple of 10 or a power of 2, use size+1, which is size because python starts indexing at 0
        if size %10 ==0 or (size & (size-1))==0:
            self.hashDivisor = size
        else:
            self.hashDivisor = size-1

    def hash(self,number):
        return number % self.hashDivisor

    def insert(self,number):
        index = self.hash(number)
        if self.array[index] == None:
            self.array[index] = linkedList(number)
        else:
            self.array[index].add(number)

    def delete(self,number,searchIncrementor=None,deleteIncrementor=None):
        if searchIncrementor:
            searchIncrementor.inc()
        linkedList = self.array[self.hash(number)]
        if linkedList:
            linkedList.deleteByKey(number,searchIncrementor,deleteIncrementor)

    def search(self,number,incrementor=None):
        linkedList = self.array[self.hash(number)]
        if linkedList:
            return linkedList.search(number,incrementor)
        else:
            return -1

h = Hash(arraySize)

for _ in range(numberOfNumbers):
    h.insert(getRand())
searchIncrementor = commonFunctions.Incrementor();
found = 0
for _ in range(numberOfNumbers):
    if h.search(getRand(),searchIncrementor) != -1:
        found+=1
print "Number of comparisons: ",searchIncrementor.getVal()
print "Number of numbers found in hashtable ", found

deleteSearchIncrementor = commonFunctions.Incrementor();
deleteFoundIncrementor = commonFunctions.Incrementor();
for _ in range(numberOfNumbers):
    h.delete(getRand(),deleteSearchIncrementor,deleteFoundIncrementor)
print "Number of searches performed: ",deleteSearchIncrementor.getVal()
print "Number of deletions ", deleteFoundIncrementor.getVal()

