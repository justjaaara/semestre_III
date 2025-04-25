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

  def route_exists(self, source_vertex, destination_vertex):
    #esta es la cola auxiliar que se va a usar para hacer el recorrido
    custom_queue = Queue()
    custom_queue.enqueue(source_vertex)
    visited = set()
    visited.add(source_vertex)

    while not custom_queue.is_empty():
        current_vertex = custom_queue.dequeue()
           
        if current_vertex == destination_vertex:
            return True

        for adjacency_vertex in self.adjacency_list[current_vertex]:
            if adjacency_vertex not in visited:
                custom_queue.enqueue(adjacency_vertex)
                visited.add(adjacency_vertex)

    return False



customgraph = Graph()
customgraph.add_vertex('A')
customgraph.add_vertex('B')
customgraph.add_vertex('C')
customgraph.add_vertex('D')
customgraph.add_vertex('E')
customgraph.add_vertex('F')
customgraph.add_vertex('G')

customgraph.add_vertex(1)
customgraph.add_vertex(2)
customgraph.add_vertex(3)
customgraph.add_vertex(4)
customgraph.add_vertex(5)
customgraph.add_vertex(6)
customgraph.add_vertex(7)

customgraph.add_edge(1,2)
customgraph.add_edge(1,3)
customgraph.add_edge(2,7)
customgraph.add_edge(3,4)
customgraph.add_edge(3,5)
customgraph.add_edge(4,3)
customgraph.add_edge(4,6)
customgraph.add_edge(5,6)
customgraph.add_edge(6,3)


customgraph.add_edge("A","B")
customgraph.add_edge("A","C")
customgraph.add_edge("B","G")
customgraph.add_edge("C","D")
customgraph.add_edge("C","E")
customgraph.add_edge("D","C")
customgraph.add_edge("D","F")
customgraph.add_edge("E","F")
customgraph.add_edge("F","D")

customgraph.print_graph()
print('Exite ruta entre C y A')
#print(customgraph.route_exists('C','A'))
print(customgraph.route_exists(3,1))
print('')
print('Exite ruta entre A y G')
#print(customgraph.route_exists('A','G'))
print(customgraph.route_exists(1,7))