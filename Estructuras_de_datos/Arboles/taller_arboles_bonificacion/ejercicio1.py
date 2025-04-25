'''
Con la clase construida en el salon para BinaryTree, escriba una función que reciba un árbol binario
y un valor a encontrar. Retorne cuántas veces está este valor en todo el árbol
omitiendo a los padres de las hojas.

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



def levelorder(rootNode):
  if not rootNode:
    return ("Arbol Vacio")
  else:
    customqueue = queue()
    customqueue.enqueue(rootNode)

    while not(customqueue.is_empty()):
      temproot = customqueue.dequeue()
      print(temproot.value.data)

      if (temproot.value.leftchild is not None):
        customqueue.enqueue(temproot.value.leftchild)

      if (temproot.value.rightchild is not None):
        customqueue.enqueue(temproot.value.rightchild)

def count_leaf_node(rootNode, value, counter = 0):
  
    if not rootNode:
        return counter
    else:
        customqueue = queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.is_empty()):
            temproot = customqueue.dequeue()
            if temproot.value.data == value:
              if temproot.value.leftchild is None and temproot.value.rightchild is None:
                counter += 1
            if temproot.value.leftchild is not None:
                customqueue.enqueue(temproot.value.leftchild)
            if temproot.value.rightchild is not None:
                customqueue.enqueue(temproot.value.rightchild)

        return counter



btree = binarytree(50)
insertNode(btree, binarytree(20))
insertNode(btree, binarytree(10))
insertNode(btree, binarytree(10))
insertNode(btree, binarytree(30))
insertNode(btree, binarytree(40))
insertNode(btree, binarytree(60))
insertNode(btree, binarytree(10))
insertNode(btree, binarytree(10))
insertNode(btree, binarytree(80))
insertNode(btree, binarytree(90))
insertNode(btree, binarytree(70))
insertNode(btree, binarytree(30))
insertNode(btree, binarytree(10))

printTree(btree)
print(f'leaf node count of node 10: {count_leaf_node(btree, 10)}')
