import quickSort,mergeSort, heapSort, insertionSort, bubbleSort, time
from commonFunctions import createRandomLists


sortFunctions = ['quickSort.startQuickSort','mergeSort.mergeSort','heapSort.heapSort','insertionSort.insertionSort','bubbleSort.bubbleSort']

randomLists = createRandomLists(5,10)
listLengths = randomLists.keys()
listLengths = mergeSort.mergeSort(listLengths) # lol


functionTimes = {}
for function in sortFunctions:
    functionTimes[function] = {}
    for listLength in listLengths:
        list = randomLists[listLength]
        start = time.time()
        eval(function)(list)
        end = time.time()
        functionTimes[function][listLength] = end-start

#print functionTimes

print "N= "+" "*(len("insertionSort")+8),
for n in listLengths:
    print str(n)+" "*(5-len(str(n))),
print ""
for function in sortFunctions:
    print function.split(".")[0],reduce(lambda x,time:str(x)+" "+str(round(time,5)),functionTimes[function].values())







    
        
