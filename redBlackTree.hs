-- based on work by Osaki and Might
-- https://wiki.rice.edu/confluence/download/attachments/2761212/Okasaki-Red-Black.pdf
-- http://matt.might.net/articles/red-black-delete/

data RBT a = DBNULL| NULL | Node Color (RBT a) a (RBT a)
     deriving (Show,Eq)

data Color = DB|B|R|NB
     deriving (Show, Eq)

isDB :: Ord a => RBT a -> Bool
isDB DBNULL = True
isDB (Node DB a x b) = True
isDB _ = False

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

redderAcceptsLeaf :: RBT a -> RBT a
redderAcceptsLeaf DBNULL = NULL
redderAcceptsLeaf (Node color left key right) = Node (redder color) left key right

blacken :: Ord a => RBT a -> RBT a
blacken NULL = NULL
blacken DBNULL = DBNULL
blacken (Node color a x b) = Node B a x b

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

-- fixBubble
-- fix double black root
balance (Node DB (Node R a x (Node R b y c)) z d) = Node B (Node B a x b) y (Node B c z d)
balance (Node DB (Node R (Node R a x b) y c) z d) = Node B (Node B a x b) y (Node B c z d)	
balance (Node DB a x (Node R (Node R b y c) z d)) = Node B (Node B a x b) y (Node B c z d)
balance (Node DB a x (Node R b y (Node R c z d))) = Node B (Node B a x b) y (Node B c z d)

-- fixNegaive black
balance (Node DB (Node NB (Node B a w b) x (Node B c y d)) z e) = Node B (Node B (balance(Node R a w b)) x c) y (Node B d z e)
balance (Node DB a z (Node NB (Node B b w c) x (Node B d y e ))) = Node B(Node B a z b) w (Node B c x (balance(Node R d y e)))

balance (Node color a x b) = Node color a x b 

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
deleteKey dKey (Node color left currentKey right) = delKey (Node color left currentKey right)
--	  where delKey NULL = NULL
	  where delKey (Node c le x ri)	  
	  	  | dKey == x = deleteNode (Node c le x ri)
		  | dKey <  x = bubble (Node c (delKey le) x ri)
		  | dKey >  x = bubble (Node c le x (delKey ri))


deleteNode :: Ord a => RBT a -> RBT a
deleteNode (Node R NULL _ NULL) = NULL
deleteNode (Node B NULL _ NULL) = DBNULL
deleteNode (Node B (Node R a x b) _ NULL) = Node B a x b
deleteNode (Node B NULL _ (Node R a x b)) = Node B a x b
deleteNode (Node color left _ right) = bubble (Node color left newKey (deleteKey newKey right)) where newKey = minKey(right)

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
       |isDB a || isDB b = balance (Node (blacker color) (redderAcceptsLeaf a) x (redderAcceptsLeaf b))
       | otherwise = balance (Node color a x b)



checkInvariantTwo :: Ord a => RBT a -> Bool
checkInvariantTwo NULL = True
checkInvariantTwo (Node R (Node R a x b) y (Node B c z d)) = False
checkInvariantTwo (Node R (Node B a x b) y (Node R c z d)) = False
checkInvariantTwo (Node R (Node R a x b) y (Node R c z d)) = False
checkInvariantTwo (Node _ l x r) = (checkInvariantTwo l) && (checkInvariantTwo r) 

distToBottomList :: (Ord a) => RBT a -> Int -> [Int]
distToBottomList (Node B l x r ) dist = (distToBottomList l (dist+1)) ++  (distToBottomList r (dist+1))
distToBottomList (Node R l x r ) dist = (distToBottomList l (dist)) ++  (distToBottomList r (dist))
distToBottomList NULL dist = [dist ]


checkInvariantOne :: Ord a => RBT a -> Bool
checkInvariantOne tree = all (== head nums) nums where 
		  nums = distToBottomList tree 0 

checkInvariants :: Ord a => RBT a -> Bool
checkInvariants tree = (checkInvariantOne tree) && (checkInvariantTwo tree)
-- checkInvariantTwo (deleteKey 6 (createFromList[50,32,2,4,3,5,6,100,99,110,111,112]))

-- checkInvariants (deleteKey 32 (insert 1001 (deleteKey 5 (deleteKey 6 (createFromList [32,5,100,2,50,6,3233])))))
