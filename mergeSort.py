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

def merge(l1,l2):
    if len(l1)==0: 
        return l2
    if len(l2)==0: 
        return l1
    if l1[0]<=l2[0]: 
        return [l1[0]]+merge(l1[1:],l2)
    if l2[0]<l1[0]: 
        return[l2[0]]+merge(l1,l2[1:])

'''
array = [-3,4,5,3,9,1,4,788,9,5,100]

print mergeSort(array)
'''
