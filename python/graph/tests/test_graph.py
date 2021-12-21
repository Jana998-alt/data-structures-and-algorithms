from graph import __version__
import pytest
from graph.graph import Graph, Vertex

def test_version():
    assert __version__ == '0.1.0'

# Node can be successfully added to the graph
def test_add_node(EmptyGraph):
  EmptyGraph.add_node("pink")
  excepted = EmptyGraph.get_nodes()
  node = Vertex("pink")
  acutual = [node.value]
  assert acutual == excepted

# An edge can be successfully added to the graph
# All appropriate neighbors can be retrieved from the graph

def test_add_edge(EmptyGraph):
  graph = EmptyGraph
  node1 = graph.add_node("black")
  node2 = graph.add_node("purple")
  graph.add_edge(node1, node2)
  actual = []
  for i in graph.get_neighbors(node1):
    actual.append(i.value)
  for i in graph.get_neighbors(node2):
    actual.append(i.value)
  excepted = [node2.value, node1.value]
  assert actual == excepted

# A collection of all nodes can be properly retrieved from the graph

def test_retrive_nodes(Graph1):
  nodes = Graph1.get_nodes()
  excepted = set(['blue', 'pink', 'black', 'purple', 'white', 'yellow'])
  actual = set(nodes)
  assert excepted == actual

# The proper size is returned, representing the number of nodes in the graph
def test_size(Graph1):
  excepted = 6
  actual = Graph1.size()
  assert excepted == actual

# test for breadth first
def test_size2(Graph2):
  excepted = {"pink", "blue"}
  actual = set(Graph2.breadth_first())

  assert excepted == actual


@pytest.fixture
def EmptyGraph():
  graph = Graph()
  return graph

@pytest.fixture
def Graph1():
  graph = Graph()
  graph.add_edge(graph.add_node("blue"),graph.add_node("pink"))
  graph.add_edge(graph.add_node("black"), graph.add_node("purple"))
  graph.add_edge(graph.add_node("white"), graph.add_node("yellow"))
  return graph

@pytest.fixture
def Graph2():
  graph = Graph()
  graph.add_edge(graph.add_node("blue"),graph.add_node("pink"))
  return graph

# @pytest.fixture
# def Graph2():
#   graph = Graph()
#   ver1 = Vertex("blue")
#   ver2 = Vertex("pink")
#   graph.add_node(ver1)
#   graph.add_node(ver2)
#   ver3 = Vertex("black")
#   ver4 = Vertex("purple")
#   ver5 = Vertex("white")
#   ver6 = Vertex("yellow")
#   graph.add_node(ver3)
#   graph.add_node(ver4)
#   graph.add_node(ver6)
#   graph.add_node(ver5)
#   graph.add_edge(ver1, ver2)
#   graph.add_edge(ver3, ver4)
#   graph.add_edge(ver5, ver6)
#   graph.add_edge(ver1, ver4)
#   graph.add_edge(ver3, ver6)
#   graph.add_edge(ver5, ver1)
#   return graph
