'''
Cormen 2.1-2: insertionSort decreasing Order
1 4 2 3
1 4 2(key) 3
1 4 3 3
1 4 3 2
1 4(key) 3 2
1(key) 4 3 2
4 4 3 2
4 3 3 2
4 3 2 2
4 3 2 1
'''

def insertionSort(numbers):
    keyIndex = len(numbers)-2
    while keyIndex >=0:
        key = numbers[keyIndex]
	i = keyIndex+1
	while i<len(numbers) and numbers[i]>key:
            numbers[i-1]=numbers[i]
            i+=1
        numbers[i-1]=key
        keyIndex-=1
    return numbers
print insertionSort([5,4,6,10,40,2,4,6,7])
