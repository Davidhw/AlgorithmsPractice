-- based on work by Osaki and Might
-- https://wiki.rice.edu/confluence/download/attachments/2761212/Okasaki-Red-Black.pdf
-- http://matt.might.net/articles/red-black-delete/

data RBT a = DBNULL| NULL | Node Color (RBT a) a (RBT a)
     deriving (Show,Eq)

data Color = DB|B|R|NB
     deriving (Show, Eq)

isBB :: RBT a -> Bool
isBB DBNULL = True
isBB (Node DB a x b) = True
isBB _ = False

blacker :: Color -> Color
blacker NB = R
blacker R = B
blacker B = DB
blacker DB = error "Can't make a double black blacker"

redder :: Color -> Color
redder DB = B
redder B = R
redder R = NB
redder NB = error "can't make a negative black redder"

blacken :: RBT a -> RBT a
blacken NULL = DBNULL
blacken (Node color a x b) = Node B a x b

redden :: RBT a -> RBT a
redden DBNULL = NULL
redden (Node color a x b) = Node (redder color) a x b


key :: Ord a => RBT a -> a
key (Node color _ a _) =  a

l :: Ord a => RBT a -> RBT a
l (Node color left _  _) =  left

r :: Ord a => RBT a -> RBT a
r (Node color _  _  right) =  right

contains :: Ord a => a -> RBT a -> Bool
contains searchKey tree
	 | search searchKey tree ==NULL = False
	 | otherwise = True

insert :: Ord a  => a -> RBT a -> RBT a
insert newKey tree = blacken (ins tree)
       where ins NULL = Node R NULL newKey NULL
       	     ins (Node color left currentKey right)
       	     	 |newKey <= currentKey = balance (Node color (ins left) currentKey right)
       	   	 | newKey > currentKey = balance (Node color left currentKey (ins right))

balance :: Ord a => RBT a -> RBT a

-- keys are x,yz
-- children are a,b,c,d
-- alphabetic order is in increasing order
-- fixInsert
balance (Node B (Node R (Node R a x b) y c) z d) = Node R (Node B a x b) y (Node B c z d)
balance (Node B (Node R a x (Node R b y c)) z d) = Node R (Node B a x b) y (Node B c z d)
balance (Node B a x (Node R b y (Node R c z d))) = Node R (Node B a x b) y (Node B c z d)
balance (Node B a x (Node R (Node R b y c) z d)) = Node R (Node B a x b) y (Node B c z d)
balance (Node color a x b) = Node color a x b 

-- fixBubble
-- fix double black root
balance (Node DB (Node R a x (Node R b y c)) z d) = Node B (Node B a x b) y (Node B c z d)
balance (Node DB (Node R (Node R a x b) y c) z d) = Node B (Node B a x b) y (Node B c z d)
balance (Node DB a x (Node R (Node R b y c) z d)) = Node B (Node B a x b) y (Node B c z d)
balance (Node DB a x (Node R b y (Node R c z d))) = Node B (Node B a x b) y (Node B c z d)

-- fixNegaive black
balance (Node DB (Node NB (Node B a w b) x (Node B c y d)) z e) = Node B (Node B (balance(Node R a w b)) x c) y (Node B d z e)
balance (Node DB a z (Node NB (Node B b w c) x (Node B d y e ))) = Node B(Node B a z b) w (Node B c x (balance(Node R d y e)))

search :: Ord a => a -> RBT a -> RBT a
search searchKey NULL = NULL
search searchKey (Node color left currentKey right)
       | currentKey == searchKey = (Node color left currentKey right)
       | currentKey < searchKey = search searchKey left
       | currentKey > searchKey = search searchKey right

minKey :: Ord a => RBT a -> a
minKey (Node color NULL currentKey _) = currentKey
minKey (Node color left currentKey right) = minKey left


deleteKey :: Ord a => a -> RBT a -> RBT a      
deleteKey _ NULL = NULL
deleteKey dKey (Node color left currentKey right)
	  | dKey == currentKey = deleteNode (Node color left currentKey right)
	  | dKey < currentKey = bubble (Node color (deleteKey dKey left) currentKey right)
	  | dKey > currentKey = bubble (Node color left currentKey (deleteKey dKey right))


deleteNode :: Ord a => RBT a -> RBT a
deleteNode (Node color left _ NULL) = (blacken left)
deleteNode (Node color NULL _ right) = (blacken right)
deleteNode (Node color left _ right) = (Node (blacker color) left newKey (deleteKey newKey right)) where newKey = minKey(right)

inOrderList :: Ord a => RBT a -> [a]
inOrderList NULL = []
inOrderList (Node color left currentKey right) = (inOrderList left) ++ [currentKey] ++ (inOrderList right)

createFromList :: Ord a => [a] -> RBT a
createFromList [] = NULL
createFromList xs = foldr insert NULL xs

height :: Ord a => RBT a -> Integer
height NULL = 0
height (Node color left _ right) = 1 + (max (height left) (height right))

bubble :: Ord a => RBT a -> RBT a
bubble (Node color a x b)
       |isBB a || isBB b = balance (Node (blacker color) (redden a) x (redden b))
       | otherwise = balance (Node color a x b)



checkInvariantTwo :: RBT a -> Bool
checkInvariantTwo NULL = True
checkInvariantTwo (Node R (Node R a x b) y (Node B c z d)) = False
checkInvariantTwo (Node R (Node B a x b) y (Node R c z d)) = False
checkInvariantTwo (Node R (Node R a x b) y (Node R c z d)) = False
checkInvariantTwo (Node _ l x r) = (checkInvariantTwo l) && (checkInvariantTwo r) 

-- checkInvariantTwo (deleteKey 6 (createFromList[50,32,2,4,3,5,6,100,99,110,111,112]))
