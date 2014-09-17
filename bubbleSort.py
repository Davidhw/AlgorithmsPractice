from commonFunctions import swap 
#from commonFunctions import exampleArray as array

def bubbleSort(array):
    swapped = True # really should do this using do - while loop to be honest
    while(swapped == True):
        swapped = False
        print array
        index = 0
        while index < len(array)-1:
            if array[index]>array[index+1]:
                swap(array,index,index+1)
                swapped = True
            index+=1
    return array

#print bubbleSort(array)
