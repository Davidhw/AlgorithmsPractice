# Implementing Mergesort

def mergeSort(arr):
    if len(arr)==1:
        return arr
    else:
        mid = int(round((len(arr)/2)))
        return merge(
            mergeSort(arr[:mid]),
            mergeSort(arr[mid:len(arr)])
         )

def merge(arr1,arr2):
    listLengthSum = len(arr1)+len(arr2)
    ENDOFARRAY =1000000000 
    output = []
    i = 0
    j = 0
    # add placemarkers to mark the end of the array. The alternative is just doing more comparisons of the counter to the array length
    arr1.append(ENDOFARRAY)
    arr2.append(ENDOFARRAY)

    while i+j < listLengthSum:# or, more efficient, do for _ in range(listLengthSum-2)
        if arr1[i]<arr2[j]:
            output.append(arr1[i])
            i+=1
        else:
            output.append(arr2[j])
            j+=1

    # this is ugly, but we have to get rid of the place holder values
    arr1.pop() 
    arr2.pop()
    return output

array = [-3,4,5,3,9,1,4,788,9,5,100]

# should eventualy make it so that you can just call it with only one arg - the array
print mergeSort(array)
