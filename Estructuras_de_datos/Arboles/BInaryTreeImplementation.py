'''
Document with binary tree python implementation
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
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)

class Queue:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.queue]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head == None

    def enqueue(self, value):

        new_node = Node(value)

        if self.linkedlist.head == None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node

        else:
            new_node.next = None
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return 'There is no elements in the list'

        else:
            popped_node = self.linkedlist.head

            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None

            else:
                self.linkedlist.head = self.linkedlist.head.next

            popped_node.next = None
            return popped_node

class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def __str__(self, level = 0):

        ret = ' ' * level + str(self.data) + '\n'

        if self.leftchild:
            ret += self.leftchild.__str__(level + 1)

        if self.rightchild:
            ret += self.rightchild.__str__(level + 1)

        return ret

    def print_tree(self,node, prefix = '', is_left=True):
            
        if not node:
            return
        if Node.rightchild:
            self.print_tree(node.rightchild, prefix + ('│    ' if is_left else '    '), False)
        
        print(prefix + ('└── ' if is_left else '┌── ') + str(node.data))

        if node.leftchild:
            self.print_tree(node.leftchild, prefix + ('     ' if is_left else '│   '), True)

    def search_node(self,root_node, node_value):
        if not root_node:
            return 'Empty Tree'

        else:
            custom_queue = Queue()
            custom_queue.enqueue(root_node)

            while not (custom_queue.is_empty()):
                temp_root = custom_queue.dequeue()

                if temp_root.value.data == node_value:
                    return f'The node with value {node_value} was found'

                if temp_root.value.leftchild is not None:
                    if temp_root.value.leftchild.data == node_value:
                        return f'The node with value {node_value} was found'

                    else:
                        custom_queue.enqueue(temp_root.value.leftchild)

                if temp_root.value.rightchild is not None:
                    if temp_root.value.rightchild.data == node_value:
                        return f'The node with value {node_value} was found'

                    else:
                        custom_queue.enqueue(temp_root.value.rightchild)

            return f'The node with value {node_value} was not found'

    def insert_node(self,root_node,new_node):

        if not root_node:
            root_node = new_node

        else:
            custom_queue = Queue()
            custom_queue.enqueue(root_node)

            while not (custom_queue.is_empty()):
                temp_root = custom_queue.dequeue()

                if temp_root.value.leftchild is None:
                    temp_root.value.leftchild = new_node
                    return 'Node inserted'
                custom_queue.enqueue(temp_root.value.leftchild)

                if temp_root.value.rightchild is None:
                    temp_root.value.rightchild = new_node
                    return 'Node inserted'
                custom_queue.enqueue(temp_root.value.rightchild)

    def find_deepest_node(self,root_node):

        if not root_node:
            return 'Empty Tree'

        else:
            custom_queue = Queue()
            custom_queue.enqueue(root_node)

            while not (custom_queue.is_empty()):
                temp_root = custom_queue.dequeue()

                if temp_root.value.leftchild is not None:
                    custom_queue.enqueue(temp_root.value.leftchild)
                
                if temp_root.value.rightchild is not None:
                    custom_queue.enqueue(temp_root.value.rightchild)

            return temp_root.value

    def delete_node(self, root_node, node_value):
        if not root_node:
            return 'Empty Tree'
        else:
            custom_queue = Queue()
            custom_queue.enqueue(root_node)

            while not custom_queue.is_empty():
                temp_root = custom_queue.dequeue()

                if temp_root.value.data == node_value:
                    deepest_node = self.find_deepest_node(root_node)
                    temp_root.value.data = deepest_node.data
                    self.delete_deepest_node(root_node,deepest_node)
                    return f'The node with value {node_value} was deleted'

                if temp_root.value.leftchild is not None:
                    custom_queue.enqueue(temp_root.value.leftchild)
                
                if temp_root.value.rightchild is not None:
                    custom_queue.enqueue(temp_root.value.rightchild)

            return f'The node with value {node_value} was not found'

    def delete_deepest_node(self, root_node, deepest_node):
        if not root_node:
            return 'Empty Tree'
        else:
            custom_queue = Queue()
            custom_queue.enqueue(root_node)

            while not custom_queue.is_empty():
                temp_root = custom_queue.dequeue()

                if temp_root.value is deepest_node:
                    temp_root = None
                
                if temp_root.value.leftchild is not None:
                    if temp_root.value.leftchild is deepest_node:
                        temp_root.value.leftchild = None
                        return 
                    else:
                        custom_queue.enqueue(temp_root.value.leftchild)

                if temp_root.value.rightchild is not None:
                    if temp_root.value.rightchild is deepest_node:
                        temp_root.value.rightchild = None
                        return

                    else:
                        custom_queue.enqueue(temp_root.value.rightchild)


    def delete_binary_tree(self, root_node):
        root_node.data = None
        root_node.leftchild = None
        root_node.rightchild = None
        return 'Binary Tree Deleted'
