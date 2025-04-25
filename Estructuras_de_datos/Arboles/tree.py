'''
Binary Tree implementation
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
      return popped_node

class binarytree:
  def __init__(self,data):
    self.data = data
    self.leftchild = None
    self.rightchild = None




def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)
    
def search_node(root_node, node_value):
  
  if not root_node:
    return f'El nodo con valor {node_value} no fue encontradp'

  else:
    custom_queue = queue()
    custom_queue.enqueue(root_node)

  while not custom_queue.is_empty():
    current = custom_queue.dequeue()

    if current.value.data == node_value:
      return f'El nodo con valor {node_value} fue encontrado'

    else:
      if current.value.leftchild:
        if current.value.leftchild.data == node_value:
            return f'El nodo con valor {node_value} fue encontrado'
        else:
          custom_queue.enqueue(current.value.leftchild)
      if current.value.rightchild:
        if current.value.rightchild.data == node_value:
            return f'El nodo con valor {node_value} fue encontrado'
        else:
          custom_queue.enqueue(current.value.rightchild)

newbt = binarytree("Libros")
fantasia = binarytree("fantasia")
fantasia.leftchild = binarytree("epica")
fantasia.rightchild = binarytree("urbana")

comedia = binarytree("comedia")
comedia.leftchild = binarytree("romantica")
comedia.rightchild = binarytree("negra")

newbt.leftchild = fantasia
newbt.rightchild = comedia

print(newbt)
print(search_node(newbt,"heroica"))