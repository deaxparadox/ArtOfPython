# Python program to see if two trees are identical
# using DFS
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to check if two trees are identical
def isIdentical(r1, r2):

    # If both trees are empty, they are identical
    if r1 is None and r2 is None:
        return True

    # If only one tree is empty, they are not identical
    if r1 is None or r2 is None:
        return False

    # Check if the root data is the same and
    # recursively check for the left and right subtrees
    return (r1.data == r2.data and
            isIdentical(r1.left, r2.left) and
            isIdentical(r1.right, r2.right))

if __name__ == "__main__":

    # Representation of input binary tree 1
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)

    # Representation of input binary tree 2
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(3)
    r2.left.left = Node(4)

    if isIdentical(r1, r2):
        print("Yes")
    else:
        print("No")