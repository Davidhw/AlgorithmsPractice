class Ring:
    def __init__(self,size):
        self.size = size

class RingStack:
    def __init__(self,location):
        self.location = location
        self.rings = []

    def size(self):
        if self.peek():
            return self.rings.size()
        else:
            return 0

    def peek(self):
        if len(self.rings)>0:        
            return self.rings[-1]
        else:
            return None

    def pop(self):
        if self.peek():
            ret = self.rings[-1]
            self.rings.remove(ret)
            return ret
        else:
            print "Can't pop from empty stack"
            return None

    def push(self,ring):
        top = self.peek()
        if top == None or ring.size<top.size:
            self.rings.append(ring)
        else:
            print "not pushing. Only a smaller ring can be placed on top of another ring."

def moveTop(moveFrom,moveTo):
    if moveFrom.peek():
        moveTo.push(moveFrom.pop())

    
stack1 = RingStack(1)
stack2 = RingStack(2)
stack3 = RingStack(3)

for num in reversed(range(4)):
    stack1.push(Ring(num+1))

# only using moveTop, move the rings from stack1 to stack3
