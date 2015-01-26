

class Node(object):
    def __init__(self,key,parent=None,left=None,right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


    def __repr__(self):
        root = self.getRoot()
        dist = str(self.distFromTop(root))
        k = str(self.key)
        return k+". "+dist

    def getRoot(self):
        if self.parent !=None:
            return self.parent.getRoot()
        else:
            return self

    def goDownOneNode(self,comparisonKey):
        currentNode = self
        if comparisonKey <= currentNode.key:
            currentNode =currentNode.left
        else:
            currentNode =currentNode.right
        return currentNode

    def insertKey(self,keyToInsert):
        # if the tree is empty, make a root with the key
            currentNode = self
            ## this while loop could be unpacked to be more efficient
            potentialNewNode = currentNode
            while potentialNewNode  !=None: 
                currentNode = potentialNewNode
                potentialNewNode = currentNode.goDownOneNode(keyToInsert)

            inserted = self.__class__(keyToInsert)
            inserted.parent = currentNode
            if currentNode.key < keyToInsert:
                print currentNode.key
                currentNode.right = inserted
            else:
                print currentNode.key
                currentNode.left = inserted
            return inserted

    def distFromTop(self,root):
        keyToFind = self.key
        dist = 0
        if root.key ==keyToFind:
            return dist
        else:
            currentNode = root
            while currentNode.key !=None:
                dist+=1
                currentNode = currentNode.goDownOneNode(keyToFind)
                if currentNode.key == keyToFind:
                    return dist
            return None
    
    def getTreeAsDict(self,depth=None,retDict=None):
        if depth is None:
            depth = 0
        if retDict is None:
            retDict = {}

        # should only happen once
        if depth not in retDict:
            retDict[depth] = []

        retDict[depth].append(self)

        children = [self.left,self.right]
        for child in children:
            if child:
                if depth+1 not in retDict:
                    retDict[depth+1] = []
                if child not in retDict[depth+1]:
                    retDict = child.getTreeAsDict(depth+1,retDict)

        return retDict
        
                    
    def printTree(self):
        dict = self.getTreeAsDict()
        for level in dict.values():            
            print " ~ ".join([str(node) for node in sorted(level,key = lambda x: x.key)])

            




    def search(self,keyToFind):
        if self.key ==keyToFind:
            return self
        else:
            currentNode = self
            while currentNode.key !=None:
                currentNode = currentNode.goDownOneNode(keyToFind)
                if currentNode.key == keyToFind:
                    return currentNode
            return None
        
    def transplant(self,nodeToReplace,replacer):
        if nodeToReplace.parent!=None:
            if nodeToReplace.parent.left == nodeToReplace:
                nodeToReplace.parent.left = replacer
            else:
                nodeToReplace.parent.right = replacer
        if replacer:
            replacer.parent = nodeToReplace.parent

               
    def deleteKey(self,keyToDelete):
        nodeToDelete = self.search(keyToDelete)
        if nodeToDelete!=None:
            ret = self.removeNode(nodeToDelete)
            return ret
        return False

    def removeNode(self,nodeToRemove):
        # removing a leaf
        if nodeToRemove.left==None and nodeToRemove.right ==None:
            self.transplant(nodeToRemove,None)
            del nodeToRemove
            return None

        # removing node with one child
        ## if statements can be branched deeper for more efficiency
        elif nodeToRemove.left!=None and nodeToRemove.right==None:
            ret = nodeToRemove.left
            self.transplant(nodeToRemove,nodeToRemove.left)
            return ret
        elif nodeToRemove.left==None and nodeToRemove.right!=None:
            ret = nodeToRemove.right
            self.transplant(nodeToRemove,nodeToRemove.right)
            return ret

        else:
            sucessor = nodeToRemove.getSuccessor()
            nodeToRemove.key = sucessor.key
            return self.removeNode(sucessor)
    
    def getSuccessor(self):
        if self.right:
            return self.right.getMin()
        elif self.left:
            return self.left.getMax()
        else:
            return None

    def getMin(self):
        currentNode = self
        while currentNode.left!=None:
            currentNode= currentNode.left
        return currentNode
        
    def getMax(self):
        currentNode = self
        while currentNode.right!=None:
            currentNode= currentNode.right
        return currentNode

def getKeysInOrder(node):
    if node == None:
        return ""
    return getKeysInOrder(node.left)+ ' '+str(node.key)+' '+getKeysInOrder(node.right)
'''
root = Node(10)
root.insertKey(1)            
root.insertKey(-1)            
root.insertKey(91)            
root.insertKey(14)            
root.insertKey(3)            
root.insertKey(100)            
print getKeysInOrder(root)
root.deleteKey(14)
print getKeysInOrder(root)
root.deleteKey(-1)
print getKeysInOrder(root)
root.deleteKey(10)
print getKeysInOrder(root)
'''
    
