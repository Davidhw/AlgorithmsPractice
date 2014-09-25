class doublyLinkedList():
    def __init__(self,key = None,prev=None,next=None):
        self.next = next
        self.prev = prev
        self.key = key

    def add(self,key):
        element = doublyLinkedList(key,self,self.next)
        if self.next:
            self.next.prev = element
        self.next = element

    def getByIndex(self,index):
        currentElement = self.next
        for i in range(index-1):
            currentElement = currentElement.next
        return currentElement

    def deleteByIndex(self,index):
        elementToDelete = self.getByIndex(index)
        elementToDelete.prev.next  = elementToDelete.next
        elementToDelete.next.prev = elementToDelete.prev
    def deleteByKey(self,key):
        self.deleteByIndex(self.search(key))


    def toString(self):
        currentElement = self
        listToString = ""
        while currentElement != None:
            listToString += str(currentElement.key)+" "
            currentElement = currentElement.next
        return listToString

    def search(self,key):
        currentElement = self
        i = 0
        while currentElement != None:
            if currentElement.key == key:
                return i
            else:
                currentElement = currentElement.next
                i+=1
        return -1
"""
head = doublyLinkedList()
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
