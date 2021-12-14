# Write a function called tree_intersection that takes two binary trees as parameters.
# Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

from hashtable import Hashtable
from trees import BinaryTree

def tree_intersection(tree1, tree2):
  # traverse the trees and keep track of each node data
  traversals_array = Hashtable()
  intersection = []

  def _inorder(root):
      if root.left != None:
          _inorder(root.left)

      if not traversals_array.contains(root.value):
        traversals_array.add(root.value, False)
      else:
        traversals_array.add(root.value, True)
        intersection.append(root.value)

      if root.right != None:
          _inorder(root.right)

  _inorder(tree1.root)
  _inorder(tree2.root)
  
  return intersection


# def depth_in_order(self, root):


#       return traversals_array
