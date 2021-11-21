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

    if root:
      if root.left != None:
        self.depth_pre_order(root.left)
        self.traversals_array.append(root.left.value)

      else:
        self.traversals_array.append(root.left.value)


      self.traversals_array.append(root.value)

      if root.right != None:
        self.depth_pre_order(root.right)
        self.traversals_array.append(root.right.value)
      else:
        self.traversals_array.append(root.right.value)

    return self.traversals_array


  def depth_post_order(self, root = None):

    if root == None:
      root = self.root
      self.traversals_array = []

    if root:
      if root.left != None:
        self.depth_post_order(root.left)
        self.traversals_array.append(root.value)


      if root.right != None:
        self.depth_post_order(root.right)
        self.traversals_array.append(root.value)


      self.traversals_array.append(root.value)


    return self.traversals_array


class BinarySearchTree:
  def __init__(self) -> None:
      self.super(BinaryTree)


# Contains
# Argument: value
# Returns: boolean indicating whether or not the value is in the tree at least once.

  def add(self,value, root = None):
    if root == None:
      self.root = Node(value)

    is_larger = (root.value > value)

    if root.right == None and is_larger:
      root.right = Node(value)

    else:
      self.add(value,root.right)

    if root.left == None and not is_larger:
      root.left = Node(value)
    else:
      self.add(value,root.left)

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
        self.contains()


    else:
      self.add(value,root.right)

    if root.left == None and not is_larger:
      root.left = Node(value)
    else:
      self.add(value,root.left)







if __name__ == "__main__":
  pass
