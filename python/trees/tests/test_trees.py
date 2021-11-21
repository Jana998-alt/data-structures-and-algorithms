from trees import __version__
import pytest

from trees.trees import (Node, BinaryTree)


def test_version():
    assert __version__ == '0.1.0'


# Can successfully instantiate an empty tree

def test_for_instantiation():
  new_tree = BinaryTree()
  excepted = None
  actual = new_tree.root
  assert excepted == actual

# Can successfully instantiate a tree with a single root node

def test_for_instantiation_with_root():
  new_tree = BinaryTree('First Node')
  excepted = "First Node"
  actual = new_tree.root.value
  assert excepted == actual

# Can successfully add a left child and right child to a single root node

def test_for_adding_left_amd_right_to_root():
  new_tree = BinaryTree('First Node')
  new_tree.root.add_right("potato")
  new_tree.root.add_left("pizza")

  excepted = "First Node: potato and pizza"
  actual = f"{new_tree.root.value}: {new_tree.root.right.value} and {new_tree.root.left.value}"
  assert excepted == actual

# Can successfully return a collection from a preorder traversal

def test_for_preorder(tree):
  excepted = ['a', 'c', 'g', 'h','f','b','e','d']
  actual = tree.depth_pre_order()
  assert excepted == actual


# Can successfully return a collection from an inorder traversal

def test_for_In_order(tree):
  excepted = ['g','h', 'c', 'f', 'a','e','b','d']
  actual = tree.depth_in_order()
  assert excepted == actual


# Can successfully return a collection from a postorder traversal

def test_for_post_order(tree):
  excepted = ['h','g', 'f', 'c', 'a','e','d','b']
  actual = tree.depth_post_order()
  assert excepted == actual

@pytest.fixture
def tree():
  new_tree = BinaryTree('a')
  new_tree.root.add_right("b")
  new_tree.root.add_left("c")
  new_tree.root.right.add_right("d")
  new_tree.root.right.add_left("e")
  new_tree.root.left.add_right("f")
  new_tree.root.left.add_left("g")
  new_tree.root.left.left.add_right("h")
  return new_tree

# a
# c   b
# gf   ed
#  h
