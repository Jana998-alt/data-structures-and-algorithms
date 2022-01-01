from graph import __version__
import pytest
from graph.graph import Graph, Vertex
from graph.Queue import Node
from graph.graph import business_trip

def test_version():
    assert __version__ == '0.1.0'

# Node can be successfully added to the graph
def test_add_node(EmptyGraph):
  EmptyGraph.add_node("pink")
  excepted = EmptyGraph.get_nodes()
  node = Node("pink")
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
def test_breadth_first2(Graph2):
  excepted = {"pink", "blue"}
  actual = set(Graph2.breadth_first())

  assert excepted == actual

def test_breadth_first3(Graph3):
  excepted = {"pink", "blue", "black", "purple", "white", "yellow"}
  actual = set(Graph3.breadth_first())

  assert excepted == actual

def test_business_trip1(trip_graph):

  excepted = (True, "$82")
  actual = business_trip(trip_graph, ["Metroville", "Pandora", ])

  assert excepted == actual

def test_business_trip2(trip_graph):

  excepted = (True, "$115")
  actual = business_trip(trip_graph,["Arendelle", "New Monstropolis", "Naboo"])

  assert excepted == actual

def test_business_trip3(trip_graph):

  excepted = (False, "$0")
  actual = business_trip(trip_graph, ["Naboo", "Pandora"])

  assert excepted == actual

def test_business_trip4(trip_graph):

  excepted = (False, "$0")
  actual = business_trip(trip_graph, ["Narnia", "Arendelle", "Naboo"])

  assert excepted == actual

def test_depth_first(depth_graph):
  graph, node = depth_graph
  expected = ["A", "B", "C", "G", "D", "E", "H", "F"]
  actual = graph.depth_first(node)
  assert expected == actual

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

@pytest.fixture
def Graph3():
  graph = Graph()
  ver1 = Node("blue")
  ver2 = Node("pink")
  graph.add_node(ver1)
  graph.add_node(ver2)
  ver3 = Node("black")
  ver4 = Node("purple")
  ver5 = Node("white")
  ver6 = Node("yellow")
  graph.add_node(ver3)
  graph.add_node(ver4)
  graph.add_node(ver6)
  graph.add_node(ver5)
  graph.add_edge(ver1, ver2)
  graph.add_edge(ver3, ver4)
  graph.add_edge(ver5, ver6)
  graph.add_edge(ver1, ver4)
  graph.add_edge(ver3, ver6)
  graph.add_edge(ver5, ver1)
  return graph

@pytest.fixture
def trip_graph():
  graph = Graph()

  ver1 = Node("Pandora")
  ver2 = Node("Arendelle")
  ver3 = Node("Metroville")
  ver4 = Node("New Monstropolis")
  ver5 = Node("Narnia")
  ver6 = Node("Naboo")

  graph.add_node(ver1)
  graph.add_node(ver2)
  graph.add_node(ver3)
  graph.add_node(ver4)
  graph.add_node(ver5)
  graph.add_node(ver6)

  graph.add_edge(ver1, ver2, 150)
  graph.add_edge(ver1, ver3, 82)
  graph.add_edge(ver2, ver3, 99)
  graph.add_edge(ver2, ver4, 42)
  graph.add_edge(ver3, ver4, 105)
  graph.add_edge(ver5, ver6, 250)
  graph.add_edge(ver6, ver4, 73)
  graph.add_edge(ver6, ver3, 26)
  graph.add_edge(ver5, ver3, 37)

  return graph

@pytest.fixture
def depth_graph():

  graph = Graph()

  ver1 = Vertex("A")
  ver2 = Vertex("B")
  ver3 = Vertex("C")
  ver4 = Vertex("D")
  ver5 = Vertex("E")
  ver6 = Vertex("F")
  ver7 = Vertex("G")
  ver8 = Vertex("H")


  graph.add_node(ver1)
  graph.add_node(ver2)
  graph.add_node(ver3)
  graph.add_node(ver4)
  graph.add_node(ver5)
  graph.add_node(ver6)
  graph.add_node(ver7)
  graph.add_node(ver8)

  graph.add_edge(ver1, ver2)
  graph.add_edge(ver1, ver4)
  graph.add_edge(ver2, ver3)
  graph.add_edge(ver2, ver4)
  graph.add_edge(ver3, ver7)
  graph.add_edge(ver4, ver5)
  graph.add_edge(ver4, ver8)
  graph.add_edge(ver4, ver6)
  graph.add_edge(ver6, ver8)

  return graph, ver1
