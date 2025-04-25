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
  
  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = None
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

class queue:

  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.linkedlist]
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

  def __str__(self):
    result = [str(x.value) for x in self.linkedlist]
    return ' '.join(result)



class binarytree:
  def __init__(self,data):
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

def insertNode(rootNode, newNode):
  if not rootNode:
    rootNode = newNode
    return "nodo insertado correctamente"
  else:
    customqueue = queue()
    customqueue.enqueue(rootNode)

    while not(customqueue.is_empty()):
      temproot = customqueue.dequeue()

      if temproot.value.leftchild is None:
         temproot.value.leftchild = newNode
         return "nodo insertado correctamente"
      customqueue.enqueue(temproot.value.leftchild)

      if temproot.value.rightchild is None:
        temproot.value.rightchild = newNode
        return "nodo insertado correctamente"
      customqueue.enqueue(temproot.value.rightchild)


def sumatoria_por_nivel_de_arbol(root_node):
  
  auxiliar_linkedlist = LinkedList()

  if not root_node:
    return


def levelorder(rootNode):
  if not rootNode:
    return ("Arbol Vacio")
  else:
    customqueue = queue()
    customqueue.enqueue(rootNode)
      
    auxiliar_linkedlist = LinkedList()

    while not(customqueue.is_empty()):
      temproot = customqueue.dequeue()
      print(customqueue)
      print("--------------------------------------------------------------------")
      print(temproot.value.data)

      if (temproot.value.leftchild is not None):
        customqueue.enqueue(temproot.value.leftchild)

      if (temproot.value.rightchild is not None):
        customqueue.enqueue(temproot.value.rightchild)

tree = binarytree(6)
insertNode(tree, binarytree(3))
insertNode(tree, binarytree(8))
insertNode(tree, binarytree(4))
insertNode(tree, binarytree(10))
insertNode(tree, binarytree(1))
insertNode(tree, binarytree(2))

printTree(tree)
print("---------------")
levelorder(tree)