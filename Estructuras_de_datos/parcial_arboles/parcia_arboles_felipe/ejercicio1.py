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

class BSTNode:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None

  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"

    if self.leftchild:
      ret += self.leftchild.__str__(level+1)

    if self.rightchild:
      ret += self.rightchild.__str__(level+1)

    return ret

def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)

def insertNode(rootNode, value):

  if rootNode.data == None:
    rootNode.data = value
  elif value < rootNode.data:
    if rootNode.leftchild is None:
      rootNode.leftchild = BSTNode(value)
    else:
      insertNode(rootNode.leftchild, value)
  else:
    if rootNode.rightchild is None:
      rootNode.rightchild = BSTNode(value)
    else:
      insertNode(rootNode.rightchild, value)

def n_esimo_elemento_mayor(root_node, n_esimo_element):
  
  if root_node.rightchild.data < root_node.data:
    return "No es un arbol binario de busqueda"

  else:
    auxiliar_queue = queue()
    



tree = BSTNode(8)
insertNode(tree, 4)
insertNode(tree, 12)
insertNode(tree, 2)
insertNode(tree, 6)
insertNode(tree, 10)
insertNode(tree, 14)
insertNode(tree, 1)
insertNode(tree, 3)
insertNode(tree, 9)
insertNode(tree, 11)

printTree(tree)