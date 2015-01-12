import random

class Ring:
    def __init__(self,size):
        self.size = size

class RingStack:
    def __init__(self,location):
        self.location = location
        self.rings = []

    def __str__(self):
        return ",".join([str(ring.size) for ring in self.rings])

    def size(self):
        if self.peek():
            return len(self.rings)
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

def printState():
        print "printing stacks"
        print "Stack1:",stack1
        print "Stack2:",stack2
        print "Stack3:",stack3

def moveTop(moveFrom,moveTo):
    if moveFrom.peek():
        moveTo.push(moveFrom.pop())
    else:
        print "can't move the top of an empty stack"

# using only moveTop, move the rings from stack1 to stack3    
# SOLUTION
def move(sourceStack, destStack, intermediateStack, numberOfRings):
    if numberOfRings ==1:
        moveTop(sourceStack,destStack)
    else:
        # move all but the bottom one to the intermediate stack
        move(sourceStack, intermediateStack, destStack, numberOfRings-1)
        # move the bottom one to the destination stack
        move(sourceStack, destStack, intermediateStack, 1)
        # move the ones that were above the bottom one to the destination stack
        move(intermediateStack, destStack, sourceStack, numberOfRings-1)

# RUN SOLUTION
stack1 = RingStack(1)
stack2 = RingStack(2)
stack3 = RingStack(3)

numberOfRings = random.randint(1,20)
for num in reversed(range(numberOfRings)):
    stack1.push(Ring(num+1))


printState()
move(stack1, stack3, stack2, stack1.size())
printState()
assert stack3.size() == numberOfRings, "Not all the rings were moved from stack1 to stack 3"
if numberOfRings >1:
    assert reduce(lambda ring1, ring2: ring1<ring2,stack3.rings) == True,"One ring is on top of a smaller ring."


    

