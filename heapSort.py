import math
NUMCHILDREN = 2
PLACEHOLDER = 999 # we shift our arrays over by one to make them 1 indexed so that the math works more cleanly

class Heap:
    # build max heap
    def __init__(self,a):
        self.size = len(a)+1
        a = [PLACEHOLDER]+a
        self.a = a

        parentIndex = int(math.floor(len(a)/NUMCHILDREN))
        while parentIndex >0: # can make into a do while loop
            maxHeapify(self,parentIndex)
            parentIndex = parentIndex-1

def parent(a,i):
    return int(round(i/NUMCHILDREN))

def getLeft(i):
    return i*NUMCHILDREN

def getRight(i):
    return i*NUMCHILDREN+1

# assumes left(i) and right(i) are max-heaps but that A[i] might be smaller than it's children. Lets A[i] float down in the max-heap so that the sub-tree at root i obeys the max-heap property

def maxHeapify(heap,i):
    leftInd = getLeft(i)
    rightInd = getRight(i)

    if leftInd< heap.size and heap.a[leftInd]>heap.a[i]:
        largest = leftInd
    else:
        largest = i

    if rightInd<heap.size and heap.a[rightInd] > heap.a[largest]:
        largest = rightInd

#    print "(",heap.a[largest],")"

    if largest != i:
        swap(heap.a,i,largest)
        maxHeapify(heap,largest)
        
def heapSort(array):
    heap = Heap(array)
    for element in range(len(heap.a)-1,1,-1):
        print "HEAP"    
        printTree(heap.a)
        heap.a = swap(heap.a, 1,element)
        heap.size = heap.size-1
        print "Swapped"    
        printTree(heap.a)
        maxHeapify(heap,1)

    return heap.a[1:]
                    

def swap(array, ind1, ind2):
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp
    return array
        

def printTree(array):
    elementIndex = 1
    while elementIndex < len(array):
        numToPrintInLine = 2**(elementIndex/NUMCHILDREN)
        numSpaces = 1

        printStatement = ''
        for _ in range(numToPrintInLine):
            if elementIndex>=len(array):
                break
            printStatement += (numSpaces)* " "+str(array[elementIndex])+ (numSpaces)*" "
            elementIndex+=1
        print printStatement



print heapSort([1,4,3,5,3,9,10,2])
