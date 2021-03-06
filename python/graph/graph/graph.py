import re
from graph.Queue import Queue, Node


import random

class Vertex():
  def __init__(self, value):
      self.value = value

  def __str__(self):
      return self

class Edge():
  def __init__(self, vertex1, vertex2, weight=0):
      self.vertex1 = vertex1
      self.vertex2 = vertex2
      self.weight = weight

class Graph():

  def __init__(self):
      self.__adj_list = {}

# add node
# Arguments: value
# Returns: The added node
# Add a node to the graph
  def add_node(self, value):
    if isinstance(value, Node):
      self.__adj_list[value] = []
      return value
    elif isinstance(value, Vertex):
      self.__adj_list[value] = []
      return value
    else:
      node = Node(value)
      self.__adj_list[node] = []
      return node

  def node_exists(self, node):
    if node in self.__adj_list:
      return True

    else:
      return False
# add edge
# Arguments: 2 nodes to be connected by the edge, weight (optional)
# Returns: nothing
# Adds a new edge between two nodes in the graph
# If specified, assign a weight to the edge
# Both nodes should already be in the Graph
  def add_edge(self, start_vertex, end_vertex, weight = 0):
    if start_vertex not in self.__adj_list or end_vertex not in self.__adj_list:
      raise ValueError("nodes do not exist in this graph")

    edge = Edge(start_vertex, end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)
    self.__adj_list[end_vertex].append(edge)

  def get_node_edges(self, node):
    if isinstance(node, Vertex) or isinstance(node, Node):
      edges = self.__adj_list[node]
      return edges
    else:
      for element in self.__adj_list:
        if element.value == node:
          return self.__adj_list[element]

    raise ValueError("input does not exist in graph")

# get nodes
# Arguments: none
# Returns all of the nodes in the graph as a collection (set, list, or similar)
  def get_nodes(self):
    listed_nodes = []
    for node in self.__adj_list:
      listed_nodes.append(node.value)
    return listed_nodes

# get neighbors
# Arguments: node
# Returns a collection of edges connected to the given node
# Include the weight of the connection in the returned collection

  def get_neighbors(self, node):
    edges = self.__adj_list[node]
    neighbors = []
    for edge in edges:
      if edge.vertex1 == node:
        neighbors.append(edge.vertex2)
      elif edge.vertex2 == node:
        neighbors.append(edge.vertex1)
    return neighbors

# size
# Arguments: none
# Returns the total number of nodes in the graph

  def size(self):
    return len(self.get_nodes())

# Write the following method for the Graph class:

# breadth first
# Arguments: Node
# Return: A collection of nodes in the order they were visited.
# Display the collection

  def breadth_first(self, vertex=None):
    if vertex == None:
      vertex = random.choice(list(self.__adj_list.keys()))
    if vertex:
      nodes = []
      nodes_values = []
      breadth = Queue()
      visited = set()

      breadth.enqueue(vertex)
      visited.add(vertex)

      while not breadth.is_empty():
        front = breadth.dequeue()
        nodes.append(front)
        children = self.get_neighbors(front)
        for child in children:
          if child not in visited:
            visited.add(child)
            breadth.enqueue(child)


      for node in nodes:
        nodes_values.append(node.value)


      return nodes_values

  # Name: Depth first
  # Arguments: Node (Starting point of search)
  # Return: A collection of nodes in their pre-order depth-first traversal order
  # Program output: Display the collection

  def depth_first(self, vertex):
    if not isinstance(vertex, Vertex):
      raise ValueError("input must be a Vertex")
    self._visited = set()
    self._depth_output = []
    def _depth(vertex):
      if vertex not in self._visited:
        self._visited.add(vertex)
        self._depth_output.append(vertex.value)

      neighbors = self.get_neighbors(vertex)

      for neighbor in neighbors:
        if neighbor not in self._visited:
          self._visited.add(neighbor)
          self._depth_output.append(neighbor.value)
          _depth(neighbor)
  
    _depth(vertex)
    return self._depth_output


# Write a function called business trip
# Arguments: graph, array of city names
# Return: cost or null

def business_trip(graph, city_names):
  graph_list = graph.get_nodes()
  cost = 0

  for i in range(len(city_names)-1):

    if city_names[i] not in graph_list:
      raise ValueError("city is not defined")

    else:
      edges = graph.get_node_edges(city_names[i])

      for edge in edges:
        if edge.vertex1.value == city_names[i+1]:
          cost = cost + edge.weight

        elif edge.vertex2.value == city_names[i+1]:
          cost = cost + edge.weight



  if cost == 0:
    return (False,'$'+str(cost))

  else:
    return (True, '$'+str(cost))





# sdsf

if __name__ == "__main__":

  graph = Graph()
  graph.add_edge(graph.add_node("blue"),graph.add_node("pink"))

  print(graph.breadth_first())
