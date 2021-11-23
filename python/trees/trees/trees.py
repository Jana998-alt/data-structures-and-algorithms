import re
from trees.Queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def add_right(self, val):
        self.right = Node(val)

    def add_left(self, val):
        self.left = Node(val)


class BinaryTree:
    def __init__(self, root=None):
        if root != None:
            self.root = Node(root)
        else:
            self.root = root
        self.traversals_array = []

    # root >> left >> right
    def depth_pre_order(self, root=None):

        if root == None:
            root = self.root
            self.traversals_array = []
            self.traversals_array.append(root.value)

        if root.left != None:
            self.traversals_array.append(root.left.value)
            self.depth_pre_order(root.left)

        if root.right != None:
            self.traversals_array.append(root.right.value)
            self.depth_pre_order(root.right)

        return self.traversals_array

    # left >> root >> right

    def depth_in_order(self):

        root = self.root
        test = None
        traversals_array = []

        def _inorder(root):
            if root.left != None:
                _inorder(root.left)

            traversals_array.append(root.value)

            if root.right != None:
                _inorder(root.right)

        _inorder(root)

        return traversals_array

    def depth_post_order(self, root=None):

        if root == None:
            root = self.root
            self.traversals_array = []

        if root:
            if root.left != None:
                self.depth_post_order(root.left)

            if root.right != None:
                self.depth_post_order(root.right)

            self.traversals_array.append(root.value)

        return self.traversals_array

    def find_maximum_value(self):

        root = self.root

        if root.value == None:
            raise ValueError("tree is empty")

        self.max_number = self.root.value

        def _max(root):

            if root.value > self.max_number:
                self.max_number = root.value

            if root.left != None:
                _max(root.left)

            if root.right != None:
                _max(root.right)

        _max(root)

        return self.max_number


def breadth_first(tree):
    if not tree:
        raise ValueError('this function accepts a tree as an argumant')

    else:
        queue = Queue()
        breadth_array = []
        root = tree.root

        queue.enqueue(root)
        while queue.front != None:

            front = queue.dequeue()
            breadth_array.append(front.value)

            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)


    return breadth_array




# Write a function called breadth first
# Arguments: tree
# Return: list of all values in the tree, in the order they were encountered
# NOTE: Traverse the input tree using a Breadth-first approach

# Example

class BinarySearchTree:
    def __init__(self) -> None:
        self.super(BinaryTree)

    def add(self, value, root=None):
        if root == None:
            self.root = Node(value)

        is_larger = (root.value > value)

        if root.right == None and is_larger:
            root.right = Node(value)

        else:
            self.add(value, root.right)

        if root.left == None and not is_larger:
            root.left = Node(value)
        else:
            self.add(value, root.left)

    def contains(self, val, root=None):

        if root == None:
            root = self.root
            if root == None:
                return False

        if root.value == val:
            return True

        is_larger = (root.value > val)

        if is_larger:
            if root.right != None:
                self.contains(val, root.right)
            else:
                return False

        if not is_larger:
            if root.left != None:
                self.contains(val, root.left)
            else:
                return False




class Node_k():
    def __init__(self, value,k = 2):
        self.value = value
        for i in range(k):
            self.i = None


class K_ary_Tree:
    def __init__(self, k = 2):
            self.root = None
            self.k = k


    def depth_in_order(self):

        root = self.root
        traversals_array = []


        def _inorder(root):

            traversals_array.append(root.value)
            for i in range(self.k):
                if root.i != None:
                    _inorder(root.i)


        _inorder(root)

        return traversals_array




def fizz_buzz_tree(ktree):
    new_ktree = K_ary_Tree(ktree.k)
    root = ktree.root
    new_ktree.root = root

    def _fbtree(root):

        for i in range(ktree.k):

            if root.i %5 and root.i %3:
                new_ktree.root.i.value = "Buzz"
            elif root.i %3:
                new_ktree.root.i.value = "Fizz"
            elif root.i %5:
                new_ktree.root.i.value = "Buzz"
            else:
                new_ktree.root.i.value = str(root.i.value)

            _fbtree(root.i)


    return new_ktree



if __name__ == "__main__":

  new_tree = K_ary_Tree(3)
  new_tree.root = Node_k(1)
  new_tree.root.1 = Node_k(22)

  new_tree.depth_in_order()

