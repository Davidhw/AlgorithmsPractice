class doubleLinkedList():

    def __init__(self,key = None,prev=None,next=None):
        self.next = next
        self.prev = prev
        self.key = key

    def add(self,key):
        element = doubleLinkedList(key,self,self.next)
        if self.next:
            self.next.prev = element
        self.next = element

    def getByIndex(self,index):
        currentElement = self
        for i in range(index):
            currentElement = currentElement.next
        return currentElement
    def deleteByIndex(self,index):
        elementToDelete = self.getByIndex(index)
        if elementToDelete.prev:
            elementToDelete.prev.next  = elementToDelete.next
        if elementToDelete.next:
            elementToDelete.next.prev = elementToDelete.prev
    def deleteByKey(self,key,searchIncrementor=None,deleteIncrementor=None):
        index = self.search(key,searchIncrementor)
        if index!=-1:
            if deleteIncrementor:
                deleteIncrementor.inc()
            self.deleteByIndex(index)


    def toString(self):
        currentElement = self
        listToString = ""
        while currentElement != None:
            listToString += str(currentElement.key)+" "
            currentElement = currentElement.next
        return listToString

    def search(self,key,incrementor=None):
        currentElement = self
        i = 0
        while currentElement != None:
            # keeps track of number of comparisons
            if incrementor:
                incrementor.inc()

            if currentElement.key == key:
                return i
            else:
                currentElement = currentElement.next
                i+=1
        return -1
"""
head = doubleLinkedList()
head.add(8)
head.add(3)
head.add(4)
head.add(1)
print head.toString()
head.deleteByIndex(3)
print head.toString()
print head.search(4)
head.deleteByKey(4)
print head.toString()
"""
