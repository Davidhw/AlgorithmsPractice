from binarySearchTree import Node, getKeysInOrder

RED = True
BLACK = False

def isBlack(node):
    if node == None or node.color == BLACK:
        return True
    else:
        return False

class RBNode(Node):
    def __init__(self,key,color=BLACK):
        super(self.__class__,self).__init__(key)
        self.color = color


    def __repr__(self):
        root = self.getRoot()
        k = str(self.key)
        if self.color:
            c = "red"
        else:
            c = "black"
        return k+". "+c 

    
    def grandParent(self):
        if self.parent:
            if self.parent.parent:
                return self.parent.parent

    def uncle(self):
        if self.grandParent():
                if self.grandParent().left == self.parent:
                    uncle = self.grandParent().right
                elif self.grandParent().right == self.parent:
                    uncle = self.grandParent().left
                else:
                    print "Error, parent is not a child of grandparent."
                return uncle

    def sibling(self):
        if self == self.parent.left:
            return self.parent.right
        else:
            return self.parent.left

    # unfortunately I can't just override delete key
    # i have to override removeNode as well because I have to keep track of the colors and childern of what I delete to know if I need to call fixDeletion
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
            if nodeToRemove.color == BLACK:
                nodeToRemove.fixDeletion()
            del nodeToRemove
            return None

        # replacing with right child
        elif nodeToRemove.left!=None and nodeToRemove.right==None:
            ret = nodeToRemove.left
            self.transplant(nodeToRemove,nodeToRemove.left)
            if nodeToRemove.color == BLACK:
                if ret.color == RED:
                    ret.color = BLACK
                else:
                    ret.fixDeletion()
            return ret

        # replacing with left child
        elif nodeToRemove.left==None and nodeToRemove.right!=None:
            ret = nodeToRemove.right
            self.transplant(nodeToRemove,nodeToRemove.right)
            if nodeToRemove.color == BLACK:
                if ret.color == RED:
                    ret.color = BLACK
                else:
                    ret.fixDeletion()
            return ret

        # 2 kids, swapping keys with sucessor and recursively deleting succ
        else:
            sucessor = nodeToRemove.getSuccessor()
            nodeToRemove.key = sucessor.key
            return self.removeNode(sucessor)

    def rotate(self):
        if self.parent is None:
            return

       # move up to parent's spot
        oldParentKey = self.parent.key
        self.parent.key = self.key
        self.key = oldParentKey

        if self.parent.left == self:
            # take your left child with you
            self.parent.left = self.left
            if self.left:
                self.left.parent = self.parent

            # give parent your old right child as its left child
            self.left = self.right

            # let parent take its right child with it
            self.right = self.parent.right

            # ensure parent's children consider parent their parent
            if self.left:
                self.left.parent = self
            if self.right:
                self.right.parent = self
            
            # make parent your right child
            self.parent.right = self

        elif self.parent.right == self:
            # take your right child with you
            self.parent.right = self.right
            if self.right:
                self.right.parent = self.parent

            # give parent your old left child as its right child
            self.right = self.left

            # let parent take its left child with it
            self.left = self.parent.left

            # ensure parent's children consider parent their parent
            if self.left:
                self.left.parent = self
            if self.right:
                self.right.parent = self

            # make parent your left child
            self.parent.left = self

        else:
            print "ERROR, self is not parent's child"

    def fixDeletion(self):
        # case 1, current node is root
        if self.parent == None:
            return
        
        # case 2, sibling is red
        sibling = self.sibling()
        if sibling and sibling.color == RED:
            # rotate already swaps p and s 's colors
            sibling.rotate()

        # case 3, parent, sibling, and sibling's children are black
        sibling = self.sibling()
        if isBlack(self.parent)and isBlack(sibling) and sibling and isBlack(sibling.left) and isBlack(sibling.right):
            sibling.color == RED
            self.parent.fixDeletion()
            return
    
        # case 4 red parent and black sibling/sibling's childrens
        sibling = self.sibling()
        if isBlack(sibling) and sibling and isBlack(sibling.left) and isBlack(sibling.right) and self.parent.color == RED:
            sibling.color = RED
            self.parent.color = BLACK
            return

        # case 5: sibling is black, sibling's child closest to self is red, sibling.ri is black
        sibling = self.sibling()
        # trivially true because of case 2
        if isBlack(sibling):
            if self == self.parent.left and sibling and isBlack(sibling.right) and sibling.left and sibling.left.color == RED:
                sibling.left.rotate()
                
            elif self == self.parent.right and sibling and isBlack(sibling.left) and sibling.right and sibling.right.color == RED:
                sibling.right.rotate()
        
        # case six: s is black, silbing's child farthest from self is red
        silbing = self.sibling()
        if self == self.parent.left:
            if sibling and sibling.right:
                sibling.right.color = BLACK
                sibling.rotate()
        else:
            if sibling and sibling.left:
                sibling.left.color = BLACK
                sibling.rotate()

    def fixInsertion(self):
        #(cases as outlined on wikipedia)
        # case 1, current node is root
        if self.parent == None:
            print "case 1"
            self.color = BLACK
            return

        # case 2. black parent. nothing need be done 
        if self.parent.color ==BLACK:
            print "case 2"
            return

        # case 3 red parent and uncle
        uncle = self.uncle()
        gp = self.grandParent()
        if uncle and uncle.color ==RED:
            print "case 3"
            self.parent.color = uncle.color = BLACK
            gp.color = RED
            gp.fixInsertion()
            return

        #c cases 4 and 5 red parent and black uncle
#        if self.parent and self.parent.color == RED and (self.uncle() == None or self.uncle().color ==BLACK):
        if self.grandParent() and ((self.parent.left == self) != (self.grandParent().left == self.parent)):
            print "case 4"
            self.rotate()
            self.fixInsertion()
            return

        else:
            # case 5 red parent and black uncle, 
            print "case 5"
            self.parent.rotate()
            return


    def insertKey(self,key):
        insertedNode = super(self.__class__,self).insertKey(key)
        print insertedNode.parent.key
        insertedNode.color = RED
        insertedNode.fixInsertion()
        return insertedNode
    
    def insertKeyAndGetRoot(self,key):
        return self.insertKey(key).getRoot()
'''
#import pdb
root = RBNode(10,BLACK)


print getKeysInOrder(root)
root = root.insertKey(1).getRoot()
print getKeysInOrder(root)

root = root.insertKeyAndGetRoot(-1)
print getKeysInOrder(root)

root = root.insertKeyAndGetRoot(-2)
print getKeysInOrder(root)
root = root.insertKeyAndGetRoot(-3)
print getKeysInOrder(root)
root = root.insertKeyAndGetRoot(91)
root = root.insertKeyAndGetRoot(14)
root = root.insertKeyAndGetRoot(3)
print getKeysInOrder(root)
root = root.insertKeyAndGetRoot(100)
root = root.insertKeyAndGetRoot(-4)
root.printTree()
#pdb.set_trace()
root.deleteKey(14)
root.printTree()
root.deleteKey(-1)
root.printTree()
root.deleteKey(10)
root.printTree()
root.deleteKey(-2)
root = root.insertKeyAndGetRoot(7)
root = root.insertKeyAndGetRoot(-5)
root = root.insertKeyAndGetRoot(10)
root.printTree()
root.deleteKey(7)
root.printTree()
root.deleteKey(91)
root.printTree()
'''
