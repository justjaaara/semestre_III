'''
Verificar que se pueda llevar de un vertice dado a otro vertice dado
'''

class Node:

    __slots__ = 'value', 'next'

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)

class Queue:

    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.Queue]

    def is_empty(self):
        return self.linked_list.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            new_node.next = None
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return 'No hay elementos en la lista'
        else:
            popped_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            popped_node.next = None
            return popped_node.value
          

class Stack:
  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.linkedlist]
    return ' '.join(result)

  def is_empty(self):
    return self.linkedlist.head == None

  def push(self, e):
    new_node = Node(e)
    if self.linkedlist.head == None:
      self.linkedlist.head = new_node
      self.linkedlist.tail = new_node
    else:
      new_node.next = self.linkedlist.head
      self.linkedlist.head = new_node


  def pop(self):

    if self.linkedlist.head == None:
      return None

    popped_node = self.linkedlist.head
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

  def route_exists_between(self, source_vertex, destination_vertex):
    
    if source_vertex not in self.adjacency_list or destination_vertex not in self.adjacency_list:
      return False
    

    visitted_vertex = set()
    auxiliar_stack = Stack()
    auxiliar_stack.push(source_vertex)
    visitted_vertex.add(source_vertex)

    while not auxiliar_stack.is_empty():
       
       current_vertex = auxiliar_stack.pop()

       if current_vertex == destination_vertex:
          return True

       for vertex in self.adjacency_list[current_vertex]:
          if vertex not in visitted_vertex:
             auxiliar_stack.push(vertex)
             visitted_vertex.add(vertex)

    return False
  
custom_graph = Graph()

custom_graph.add_vertex('A')
custom_graph.add_vertex('B')    
custom_graph.add_vertex('C')    
custom_graph.add_vertex('D')    
custom_graph.add_vertex('E')    

custom_graph.add_edge('A', 'B')
custom_graph.add_edge('A', 'C')

custom_graph.add_edge('B', 'E')

custom_graph.add_edge('C', 'D')
custom_graph.add_edge('C', 'A')

custom_graph.add_edge('D','E')

custom_graph.add_edge('E', 'B')

custom_graph.print_graph()

print(custom_graph.route_exists_between('A', 'E')) # True

print(custom_graph.route_exists_between('B', 'D')) # False