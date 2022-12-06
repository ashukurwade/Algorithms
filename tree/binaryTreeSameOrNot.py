#program to determine if two trees are identical

# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

#two trees, return true if they are structurally identical
def identicalTrees(a, b):

	#Both empty
	if a is None and b is None:
		return True

	#Both non-empty -> Compare them
	if a is not None and b is not None:
		return ((a.data == b.data) and
				identicalTrees(a.left, b.left)and
				identicalTrees(a.right, b.right))

	#one empty, one not -- false
	return False

root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

# Function call
if __name__ == "__main__":
    if identicalTrees(root1, root2):
	    print("Both trees are identical")
else:
	print("Trees are not identical")