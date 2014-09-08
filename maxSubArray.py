# Cormen 4.1-3
# contains both the recursive solution and the bruteforce solution(bruteForce)
# profiles them to see at which preforms best for different problem sizes

# I found that my recursive solution typically out performs my bruteforce solution for n>1, although there is a fair amount of variation between each run and sometimes various values of n >1 are still faster under the bruteforce solution. Making the recursive solution call the bruteforce solution at n =1 did not change that.

import time,math,timeit,random

#numbers = [1,-3,3,5,-32,6,2,0,10,-1,-5, 4]

SUM = 2

def findMaxCrossingSA(a,low,mid,high):
    leftSum = -100000000000000000000000000000000000000000000000 
    sum = 0
    leftIndex = mid
    maxLeftIndex = leftIndex
    while leftIndex>-1:
        sum+=a[leftIndex]        
        if sum > leftSum:
            leftSum = sum
            maxLeftIndex = leftIndex
        leftIndex = leftIndex-1

    sum = 0
    rightIndex = mid
    rightSum = -100000000000000000000000000000000000000000000000 
    while rightIndex<len(a):
        sum+=a[rightIndex]
        if sum>rightSum:
            rightSum = sum
            maxRightIndex = rightIndex
        rightIndex+=1
    return (maxLeftIndex,maxRightIndex,leftSum+rightSum-a[mid])

    
def startRecursive(a):
    if len(a)==1:
        return bruteForce(a)
    else:
        return recursive(a,0,len(a)-1)

def recursive(a,low,high):
    if high ==low:
        return (low,high,a[low])
    else:
        mid = int(math.floor(0.5*(low+high)))
        leftSideIndexsAndSum = recursive(a,low,mid)
        crossIndexsAndSum = findMaxCrossingSA(a,low,mid,high)
        rightSideIndexsAndSum = recursive(a,mid+1,high)

        leftSum = leftSideIndexsAndSum[SUM]
        crossSum = crossIndexsAndSum[SUM]
        rightSum = rightSideIndexsAndSum[SUM]

        if leftSum >= rightSum and leftSum >= crossSum:
            return leftSideIndexsAndSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightSideIndexsAndSum
        else:
            return crossIndexsAndSum

def bruteForce(numbers):
    max = -100000000000000000000000000000000000000000000000 
    maxSubArray = None
    for start in range(len(numbers)):
        for end in range(start+1,start+len(numbers)+1): # not actually sure why I have to add one the second time in this line
            subArraySum = reduce(lambda x,y: x+y,numbers[start:end])
            if subArraySum>max:
                max = subArraySum
                maxStart = start
                maxEnd = end-1
    return (maxStart,maxEnd,max)

#print bruteForce(numbers)
#print startRecursive(numbers)

def randomListOfSizeN(n):
    return [random.randint(-100,100) for x in xrange(n)]

bruteTimes = []
recursiveTimes = []
for n in xrange(1,101):
    numbers = randomListOfSizeN(n)
    startBrute = time.time()
    endBrute = time.time()
    bruteTimes.append((endBrute-startBrute)*10000)

    startRec = time.time()
    endRec = time.time()
    recursiveTimes.append((endRec-startRec)*10000)

#print bruteTimes
#print recursiveTimes

for i in xrange(len(bruteTimes)):
    print "at n = "+str(i+1)+ ", rec>brut? "+ str(recursiveTimes[i]>bruteTimes[i]) + " "+str(recursiveTimes[i]-bruteTimes[i])

    
