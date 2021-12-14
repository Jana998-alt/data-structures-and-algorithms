from tree_intersection import __version__
from tree_intersection.trees import BinaryTree
from tree_intersection.tree_intersection import tree_intersection
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_for_intersection(tree1, tree2):
  actual = tree_intersection(tree1, tree2)
  expected = [100,160,125,175,200,350,500]
  assert actual == expected

@pytest.fixture
def tree1():
  tree1 = BinaryTree()
  tree1.root = 150

  tree1.root.left = 100
  tree1.root.left.right = 160
  tree1.root.left.left = 75
  tree1.root.left.right.left = 125
  tree1.root.left.right.right = 175

  tree1.root.right = 250
  tree1.root.right.left = 200
  tree1.root.right.right = 350
  tree1.root.right.right.left = 300
  tree1.root.right.right.right = 500

@pytest.fixture
def tree2():
  tree2 = BinaryTree()
  tree2.root = 42

  tree2.root.left = 100
  tree2.root.left.right = 600
  tree2.root.left.left = 15
  tree2.root.left.right.left = 160
  tree2.root.left.right.right = 200

  tree2.root.right = 350
  tree2.root.right.left = 125
  tree2.root.right.right = 175
  tree2.root.right.right.left = 4
  tree2.root.right.right.right = 500
