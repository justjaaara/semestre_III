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

def check_if_bt_is_bst(root_node):
  
  if root_node is None:
    return
  if root_node.leftchild is not None:
    if root_node.leftchild.data < root_node.data:
        check_if_bt_is_bst(root_node.leftchild)
    else:
        return "No es BST"
  if root_node.rightchild is not None:
    if root_node.rightchild.data > root_node.data:
        check_if_bt_is_bst(root_node.rightchild)
    else:
        return "No es BST"

  return "Si es BST"
  

#Caso de prueba 1 
tree = binarytree(50)
insertNode(tree, binarytree(30))
insertNode(tree, binarytree(70))
insertNode(tree, binarytree(10))
insertNode(tree, binarytree(35))
insertNode(tree, binarytree(60))
insertNode(tree, binarytree(80))

printTree(tree)
print(check_if_bt_is_bst(tree))

#Caso de prueba 2
print("--------------------------------------")
tree = binarytree(70)
insertNode(tree, binarytree(30))
insertNode(tree, binarytree(60))
insertNode(tree, binarytree(10))
insertNode(tree, binarytree(35))
insertNode(tree, binarytree(90))
insertNode(tree, binarytree(80))

printTree(tree)
print(check_if_bt_is_bst(tree))