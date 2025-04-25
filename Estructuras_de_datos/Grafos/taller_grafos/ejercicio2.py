'''
Dado un grafo dirigido y dos nodos (S y E), diseñe un algoritmo que 
retorne cuantas rutas existen de S a E.

'''


class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

class queue:

  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.queue]
    return ' '.join(result)

  def is_empty(self):
    return self.linkedlist.head == None

  def enqueue(self, e):
    new_node = Node(e)
    if self.linkedlist.head == None:
      self.linkedlist.head = new_node
      self.linkedlist.tail = new_node
    else:
      new_node.next = None
      self.linkedlist.tail.next = new_node
      self.linkedlist.tail = new_node

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la lista"
    else:
      popped_node = self.linkedlist.head
      if self.linkedlist.head == self.linkedlist.tail:
        self.linkedlist.head = None
        self.linkedlist.tail = None
      else:
        self.linkedlist.head = self.linkedlist.head.next
      popped_node.next = None
      return popped_node.value

class Graph:

  def __init__(self):
    self.adjacency_list = {}

  def print_graph(self):
    for vertex in self.adjacency_list.keys():
      print(vertex, " : ", self.adjacency_list[vertex])

  def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = []
      return True
    return False

  def add_edge(self, sourcevertex, destinationvertex):
    if sourcevertex in self.adjacency_list and destinationvertex in self.adjacency_list:
      self.adjacency_list[sourcevertex].append(destinationvertex)
      return True
    return False

  def remove_edge(self, sourcevertex, destinationvertex):
    if sourcevertex in self.adjacency_list and destinationvertex in self.adjacency_list:
      self.adjacency_list[sourcevertex].remove(destinationvertex)
      return True
    return False

  def remove_vertex(self, vertex):
     if vertex in self.adjacency_list.keys():
        del self.adjacency_list[vertex]
        for vertices in self.adjacency_list.values():
            if vertex in vertices:
               vertices.remove(vertex)
        return True
     return False

  def existent_routes_between_vertex(self, source_vertex, destination_vertex):
    
    custom_queue = queue()
    custom_queue.enqueue(source_vertex)
    visited_vertex = set()
    visited_vertex.add(source_vertex)
    routes = 0

    while not custom_queue.is_empty():
      
      
      current_vertex = custom_queue.dequeue()

        
      print(f'visitados: {visited_vertex}')
      for adjacency_vertex in self.adjacency_list[current_vertex]:
        if adjacency_vertex == destination_vertex:
            routes += 1
        if adjacency_vertex not in visited_vertex:
            custom_queue.enqueue(adjacency_vertex)
            visited_vertex.add(adjacency_vertex)

    return routes

customgraph = Graph()
customgraph.add_vertex('A')
customgraph.add_vertex('B')
customgraph.add_vertex('C')
customgraph.add_vertex('D')
customgraph.add_vertex('E')
customgraph.add_vertex('F')
customgraph.add_vertex('G')

customgraph.add_edge("A","B")
customgraph.add_edge("A","C")
customgraph.add_edge("B","G")
customgraph.add_edge("C","D")
customgraph.add_edge("C","E")
customgraph.add_edge("D","C")
customgraph.add_edge('D','G')
customgraph.add_edge("D","F")
customgraph.add_edge("E","F")
customgraph.add_edge("F","D")

customgraph.print_graph()
print('\n')
print('Cuantas ruttas hay entre C y A')
print(customgraph.existent_routes_between_vertex('C','A'))

print('\n')
print('CUantas rutas hay entre  A y G')
print(customgraph.existent_routes_between_vertex('A','G'))

