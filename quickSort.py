def startQuickSort(array):
    return quickSort(array,0,len(array)-1)

def quickSort(array,start,finish):
    if start<finish:
        mid = partition(array,start,finish)
        quickSort(array,start,mid-1)
        quickSort(array,mid+1,finish)
    return array

def partition(array,start,finish):
    pivot = array[finish]
    swapLocation = start-1
    for j in range(start,finish):
        if array[j]<=pivot:
            swapLocation+=1
            swap(array,swapLocation,j)
    array = swap(array,swapLocation+1,finish)
    return swapLocation+1
            

def swap(array,ind1,ind2):
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp
    return array

print startQuickSort([3,5,2,10,6,-2,100,3,8,4,-100])
