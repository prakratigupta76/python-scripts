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
    

print ()
print ()

# Binary search tree (BST):
print("Binary search tree (BST):")
print ()
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        # if root is None or root.data == key:
        #     return root is not None
        if root is None:
            return False
        if root.data == key:
            return True
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left and root.right is None:
                return root
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            else:
                temp = self.find_min(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)

        return root

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

bst = BST()
bst.root = bst.insert(None, 50)
bst.insert(bst.root, 30)
bst.insert(bst.root, 70)
bst.insert(bst.root, 20)
bst.insert(bst.root, 40)
bst.insert(bst.root, 60)
bst.insert(bst.root, 80)

print("Inorder travasal of BST: ")
bst.inorder(bst.root)
print ()
print ()
print(bst.search(bst.root, 40))
print(bst.search(bst.root, 100))
print()
bst.root = bst.delete(bst.root, 50)

print("Inorder travasal after deleting 50: ")
bst.inorder(bst.root)
print()
print()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insertNew(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.value:
            root.left = self.insertNew(root.left, key)
        elif key > root.value:
            root.right = self.insertNew(root.right, key)
        return root

    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.value, end=" ")
            self.in_order(root.right)
            
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


    def isBST(self, root, min_val=float('-inf'), max_val=float('inf')):
        if root is None:
            return True
        if not (min_val < root.value < max_val):
            return False
        return self.isBST(root.left, min_val, root.value) and self.isBST(root.right, root.value, max_val)

bst = BST()
bst.root = bst.insertNew(None, 40)
bst.insertNew(bst.root, 20)
bst.insertNew(bst.root, 10)
bst.insertNew(bst.root, 30)
bst.insertNew(bst.root, 60)
bst.insertNew(bst.root, 50)
bst.insertNew(bst.root, 70)
bst.insertNew(bst.root, 25)
print("print Example code inorder travarsal:")
bst.in_order(bst.root)
print()
print("Height of BST:", bst.height(bst.root))

print(bst.isBST(bst.root))
print()


bst = BST()
bst.root = bst.insertNew(None, 50)
bst.insertNew(bst.root, 30)
bst.insertNew(bst.root, 70)

bst.in_order(bst.root)
print()
print("Height of new BST:",bst.height(bst.root))


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    def printInRange(self, root, x, y):
        if root is None:
            return

        if (root.data >= x and root.data <= y):
            self.printInRange(root.left, x, y)
            print(root.data, end= " ")
            self.printInRange(root.right, x, y)
        elif (root.data >= y):
            self.printInRange(root.left, x, y)
        else:
            self.printInRange(root.right, x, y)

    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    # def printRoot2Leaf(self, root, path):
    #     if root is None:
    #         return root
    #     path = []
    #     path.append(root.data)
    #     self.printRoot2Leaf(root.left, path)
    #     self.printRoot2Leaf(root.right, path)
    #     path.remove(path[-1])

    def lca(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left_lca = self.lca(root.left, p, q)
        right_lca = self.lca(root.right, p, q)

        if left_lca and right_lca:
            return root
        
        return left_lca if left_lca else right_lca

    def find_node(self, root, key):
        """Finds and returns the node with the given key"""
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.find_node(root.left, key)
        return self.find_node(root.right, key)

    def diameter(self, root):
        # Initialize variable to store max diameter
        self.max_diameter = 0

        def height(node):
            if node is None:
                return 0
            
            # Recursively calculate height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update max diameter found so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)  # Start calculating height from the root
        return self.max_diameter

    def root_to_leaf_path(self, root):
        def dfs(node, path):
            if node is None:
                return 

            path.append(node.data)

            if node.left is None and node.right is None:
                print(" -> ".join(map(str, path)))

            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])

    def sum_of_nodes(self, root):
        if root is None:
            return 0
        return root.data + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right)

    def sum_of_leaf_nodes(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        return self.sum_of_leaf_nodes(root.left) + self.sum_of_leaf_nodes(root.right)


# Create BST
bst = BST()
bst.root = bst.insert(None, 8)
bst.insert(bst.root, 5)
bst.insert(bst.root, 3)
bst.insert(bst.root, 1)
bst.insert(bst.root, 4)
bst.insert(bst.root, 6)
bst.insert(bst.root, 10)
bst.insert(bst.root, 11)
bst.insert(bst.root, 14)
bst.insert(bst.root, 9)

# Print Inorder Traversal
bst.in_order(bst.root)
print()

# Print nodes in range 3 to 12
bst.printInRange(bst.root, 3, 12)
print()

# Find LCA
p = bst.find_node(bst.root, 9)
q = bst.find_node(bst.root, 11)

lca = bst.lca(bst.root, p, q)
if lca:
    print("Lowest Common Ancestor of 9 and 11 is:", lca.data)
else:
    print("Lowest Common Ancestor not found.")

print("Diameter of the binary tree:", bst.diameter(bst.root))  # Output:6
bst.in_order(bst.root)
print()

# Print all root-to-leaf paths
print("Root-to-leaf paths in the binary tree:")
bst.root_to_leaf_path(bst.root)

print("Sum of all nodes in the binary tree:", bst.sum_of_nodes(bst.root))

print("Sum of all leaf nodes:", bst.sum_of_leaf_nodes(bst.root))
