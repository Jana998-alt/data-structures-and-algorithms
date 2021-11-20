import re


class Node:
  def __init__(self, value) :
    self.value = value
    self.right = None
    self.left = None

  def add_right(self,val):
    self.right = Node(val)

  def add_left(self,val):
    self.left = Node(val)



class BinaryTree:
  def __init__(self, root = None):
    if root != None:
      self.root = Node(root)
    else:
      self.root = root
    self.traversals_array = []


  # root >> left >> right
  def depth_pre_order(self,root=None):

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
  def depth_in_order(self, root = None):

    if root == None:
      root = self.root
      self.traversals_array = []

      if root.left != None:
        self.traversals_array.append(root.left.value)
        self.depth_pre_order(root.left)

      self.traversals_array.append(root.value)

      if root.right != None:
        self.traversals_array.append(root.right.value)
        self.depth_pre_order(root.right)

    # if root == None:
    #   root = self.root
    #   self.traversals_array=[]

    # if root.left != None:
    #   self.depth_in_order(root.left)
    #   self.traversals_array.append(root.left.value)

    # if root.left == None:
    #   self.traversals_array.append(root.value)

    # self.traversals_array.append(root.value)

    # if root.right != None:
    #   self.depth_in_order(root.right)
    #   self.traversals_array.append(root.right.value)

    # if root.right == None:
    #   self.traversals_array.append(root.value)

    return self.traversals_array





if __name__ == "__main__":
  pass
