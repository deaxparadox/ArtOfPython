# Maximum Depth of Height of Binary Tree

# Given the binary tree, the task is to find the 
# maximum height of the tree. The hight of the tree
# is the number of edges in the tree from the root 
# to the deepest node.


# Python program to find the height of a binary 
# tree using depth-first search (DFS) approach.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None


# Returns the height which is the number of edges
# along the longest path from the root node down
# to the farthest leaf node.
def height(root):
    if root is None:
        return -1

    # Compute the height of left and right subtree
    l_height = height(root.left)
    r_height = height(root.right)
    
    return max(l_height, r_height) + 1

if __name__ == "__main__":

    # Representation of the input tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(height(root))