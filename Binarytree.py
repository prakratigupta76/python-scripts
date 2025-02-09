#implementation example code
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#creating Nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

print(root.value)
print(root.left.value)
print(root.right.value)
print(root.left.left.value)
print(root.left.right.value)
print(root.right.left.value)
print(root.right.right.value)

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# Output: 1 2 4 5 3 6
preorder(root)
print()


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Output: 4 2 5 1 6 3 7 8
inorder(root)
print()

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end= " ")

postorder(root)
# Output: 4 5 2 6 8 7 3 1
print()

#level order travarsal
from collections import deque
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end= " ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

level_order(root)

print()
print()



#print maximum value in tree:
def max_value(root):
    if not root:
        return float('-inf')
    max_left = max_value(root.left)
    max_right = max_value(root.right)
    return max(root.value, max_left, max_right)
print("Maximum value in the tree:", max_value(root))

#print minimum value in tree:
def min_value(root):
    if not root:
        return float('inf')
    min_left = min_value(root.left)
    min_right = min_value(root.right)
    return min(root.value, min_left, min_right)
print("Minimum value in the tree:", min_value(root))

# Height of binary tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

print("Height of binary tree is: ", height(root))

#Check if a binary tree is balanced.
def is_balanced(root):
    left_height = height(root.left)
    right_height = height(root.right)
    if left_height == -1:
        return -1
    if left_height == -1:
        return -1
    
    if abs(left_height - right_height) > 1:
        return -1
    return height(root) != 1
print(is_balanced(root))

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)  # Different value here!
print(is_balanced(root))

#count total nodes in binary tree
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
print("Count of total nodes is:", count_nodes(root))

#trees are identical
def are_identical(root1,root2):
    if not root1 and not root2:
        return True
    if root1 and root2 and root1.value == root2.value:
        return are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right)
    return False
print(are_identical(root,root))

# Create two different trees
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(5)  # Different value here!

print(are_identical(root1,root2))


print()
print()
print()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
#preorder Travarsal
    def pre_order(self, node):
        if node:
            print(node.data, end= " ")
            self.pre_order(node.left)
            self.pre_order(node.right)

#Inorder Travarsal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end= " ")
            self.inorder(node.right)

#postorder Travarsal
    def Post_order(self, node):
        if node:
            self.Post_order(node.left)
            self.Post_order(node.right)
            print(node.data, end= " ")

# Height of binary tree
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
#count total nodes in binary tree
    def countNodes(self, node):
        if not node:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)

#print maximum value in tree:
    def max_value(self, node):
        if not node:
            return float('-inf')
        max_left = self.max_value(node.left)
        max_right = self.max_value(node.right)
        return max(node.data, max_left, max_right)



#print maximum value in tree:
    def min_value(self, node):
        if not node:
            return float('inf')
        min_left = self.min_value(node.left)
        min_right = self.min_value(node.right)
        return min(node.data, min_left, min_right)

#example Usage:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)


print("Preorder Traversal:")
tree.pre_order(tree.root)  # Output: 1 2 4 5 3 6

print("\nInorder Traversal:")
tree.inorder(tree.root)  # Output: 4 2 5 1 3 6

print("\nPostorder Traversal:")
tree.Post_order(tree.root)  # Output: 4 5 2 6 3 1

print("/nHeight of binary tree is: ") 
print(tree.height(tree.root))  # Output: 3

print("/nCount of Nodes in binary tree is: ") 
print(tree.countNodes(tree.root))  # Output: 6

print("Maximum value in the tree:", tree.max_value(tree.root))  # Output: 6

print("Minimum value in the tree:", tree.min_value(tree.root))  # Output: 1
    