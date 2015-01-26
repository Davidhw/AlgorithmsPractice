data BST a = NULL | Node (BST a) a (BST a)
     deriving (Show,Eq)

root :: Ord a => BST a -> a
root (Node _ a _) =  a

key :: Ord a => BST a -> a
key (Node _ k _) = k

l :: Ord a => BST a -> BST a
l (Node left _  _) =  left

r :: Ord a => BST a -> BST a
r (Node _  _  right) =  right

contains :: Ord a => a -> BST a -> Bool
contains searchKey tree
	 | search searchKey tree ==NULL = False
	 | otherwise = True

insert :: Ord a  => a -> BST a -> BST a
insert newKey NULL = Node NULL newKey NULL
insert newKey (Node left currentKey right) 
       | newKey <= currentKey = (Node (insert newKey left) currentKey right)
       | newKey > currentKey = (Node left currentKey (insert newKey right))

search :: Ord a => a -> BST a -> BST a
search searchKey NULL = NULL
search searchKey (Node left currentKey right)
       | currentKey == searchKey = (Node left currentKey right)
       | currentKey < searchKey = search searchKey left
       | currentKey > searchKey = search searchKey right

minKey :: Ord a => BST a -> a
minKey (Node NULL currentKey _) = currentKey
minKey (Node left currentKey right) = minKey left


deleteKey :: Ord a => a -> BST a -> BST a      
deleteKey _ NULL = NULL
deleteKey dKey (Node left currentKey right)
	  | dKey == currentKey = deleteNode (Node left currentKey right)
	  | dKey < currentKey = (Node (deleteKey dKey left) currentKey right)
	  | dKey > currentKey = (Node left currentKey (deleteKey dKey right))


deleteNode :: Ord a => BST a -> BST a
deleteNode (Node left _ NULL) = left
deleteNode (Node NULL _ right) = right
deleteNode (Node left _ right) = (Node left newKey (deleteKey newKey right)) where newKey = minKey(right)

inOrderList :: Ord a => BST a -> [a]
inOrderList NULL = []
inOrderList (Node left currentKey right) = (inOrderList left) ++ [currentKey] ++ (inOrderList right)

createFromList :: Ord a => [a] -> BST a
createFromList [] = NULL
createFromList xs = foldr insert NULL xs

height :: Ord a => BST a -> Integer
height NULL = 0
height (Node left _ right) = 1 + (max (height left) (height right))

