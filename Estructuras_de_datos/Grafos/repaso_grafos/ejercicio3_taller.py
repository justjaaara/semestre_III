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


class stack:
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


  def has_cycle(self):

    for vertex in self.adjacency_list.keys():
      visited = set()
      if self.cycle_helper(vertex, visited):
        print("vertice con ciclo",vertex)
        return True
    return False


  def cycle_helper(self, vertex, visited):

    customstack = stack()
    customstack.push((vertex,None))

    while not customstack.is_empty():
      print("stack", customstack.linkedlist)
      print("visitados", visited)
      current_vertex, parent = customstack.pop()

      print("current",current_vertex)
      print("parent",parent)

      if current_vertex in visited and current_vertex == vertex:
        return True

      visited.add(current_vertex)

      for adjacency_vertex in self.adjacency_list[current_vertex]:
        if adjacency_vertex != parent and adjacency_vertex not in visited:
          customstack.push((adjacency_vertex,current_vertex))
        elif adjacency_vertex != parent and adjacency_vertex == vertex:
          customstack.push((adjacency_vertex,current_vertex))

    return False

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
customgraph.add_edge('G','B')
#customgraph.add_edge("C","D")
#customgraph.add_edge("C","E")
customgraph.add_edge("D","C")
customgraph.add_edge("D","F")
customgraph.add_edge("E","F")
customgraph.add_edge("F","D")

customgraph.print_graph()
print('\n')

print(customgraph.has_cycle())