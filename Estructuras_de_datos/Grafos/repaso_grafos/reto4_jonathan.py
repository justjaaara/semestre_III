class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        result = [str(x.value) for x in self]
        return ' '.join(result)

class queue:
    def __init__(self) -> None:
        self.linked_list = LinkedList()
    
    def __str__(self) -> str:

        return print(self.linked_list)
    
    def is_empty(self):
        return self.linked_list.head == None

    def enqueue(self, e):
        new_node = Node(e)
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
        
class stack:

  def __init__(self):
    self.list = []

  def __str__(self):
    return ' '.join(map(str,reversed(self.list)))

  def is_empty(self):
    return len(self.list) == 0

  def push(self, e):
    self.list.append(e)

  def pop(self):
    if self.is_empty():
      return 'no existen elementos en la pila para retornar'
    else:
      return self.list.pop()

  def top(self):
    if self.is_empty():
      return 'no existen elementos en la pila para retornar'
    else:
      return self.list[-1]

  def len(self):
    return len(self.list)

  def delete(self):
    self.list = None
    
class Graph:

    def __init__(self) -> None:
        self.adjacency_list = {}

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, " : ", self.adjacency_list[vertex])
    #Lo que está comentado a continuación es la implementación para NO PONDERADO NO DIRIGIDO
    '''    def add_vertex(self, vertex):
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = []
                return True
            return False
        
        def add_edge(self,vertex1, vertex2):
            if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
                self.adjacency_list[vertex1].append(vertex2)
                self.adjacency_list[vertex2].append(vertex1)
                return True
            return False'''

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self,source_vertex, destination_vertex):
        if source_vertex in self.adjacency_list and destination_vertex in self.adjacency_list:
            self.adjacency_list[source_vertex].append(destination_vertex)
            return True
        return False

    def remove_edge(self,vertex, edge):
     
        if vertex not in self.adjacency_list or edge not in self.adjacency_list:
            return False
        for key in self.adjacency_list:
            if vertex == key and edge in self.adjacency_list[key]:
                self.adjacency_list[key].remove(edge)
                return True

        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return False
     
        for key in self.adjacency_list:
            if vertex in self.adjacency_list[key]:
                self.adjacency_list[key].remove(vertex)

        return self.adjacency_list.pop(vertex)

    
    def count_isolated_vertices(self):
        
        isolated_vertices = 0
        keys = list(self.adjacency_list.keys())

        while keys:
            print('--------------------')
            print(keys)
            vertex = keys.pop(0)
            visited = self.DFS(vertex)
            print(visited)

            for i in visited:
                if i in keys:
                    keys.remove(i)

            isolated_vertices += 1
        print(isolated_vertices)
                
    def recursive_paths_between_vertices(self, source_vertex, destination_vertex, path = [], possible_paths = []):
    
        path = path + [source_vertex] 

        if source_vertex == destination_vertex:
            possible_paths.append(path)
        else:
            for adjacent in self.adjacency_list[source_vertex]:
                if adjacent not in path:
                    self.recursive_paths_between_vertices(adjacent, destination_vertex, path, possible_paths)

        return possible_paths
    
    def all_dfs_paths(self, source_vertex):
        paths = []
        value_list = list(self.adjacency_list[source_vertex])
        for value in value_list:
            path = self.DFS_S(value)
            path.insert(0,source_vertex)
            paths.append(path)

        return paths
    
    def DFS_S(self,source_vertex):

        visited = set()
        customstack = stack()
        customstack.push(source_vertex)
        path = []
        #python3 repaso_grafos/reto4_jonathan.py

        while not customstack.is_empty():
            current_vertex = customstack.pop()
            if current_vertex not in visited:
                path.append(current_vertex)
                visited.add(current_vertex)

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    customstack.push(adjacency_vertex)

        return path
    
    def all_bfs_paths(self, source_vertex):
        paths = []
        value_list = list(self.adjacency_list[source_vertex])
        for value in value_list:
            path = self.BFS_S(value)
            path.insert(0,source_vertex)
            paths.append(path)

        return paths
    
    def BFS_S(self, source_vertex):
        visited = set()
        customqueue = queue()
        customqueue.enqueue(source_vertex)
        path = []
        #python3 repaso_grafos/reto4_jonathan.py

        while not customqueue.is_empty():
            current_vertex = customqueue.dequeue()
            if current_vertex not in visited:
                path.append(current_vertex)
                visited.add(current_vertex)

            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    customqueue.enqueue(adjacency_vertex)

        return path


    # Encontrar todos los caminos hacia un vertice destino
    def find_paths(self, source_vertex, destination_vertex):
        paths = []
        custom_customstack = stack()
        custom_customstack.push(source_vertex)
        path = []
        visited = set()
        
        while custom_customstack.len() > 0:
            current_vertex = custom_customstack.pop()
            if current_vertex == destination_vertex:
                path.append(current_vertex)
                paths.append(list(path))
                path.pop()
                visited.remove(current_vertex)
            else:
                path.append(current_vertex)
                for adjacency_vertex in self.adjacency_list[current_vertex]:
                    if adjacency_vertex not in visited:
                        custom_customstack.push(adjacency_vertex)
                        visited.add(adjacency_vertex)
        return paths
    
    def find_shortest_path(self,source_vertex, destination_vertex):

        paths = self.find_paths(source_vertex, destination_vertex)
        shortest = 9999

        for path in paths:
            if len(path) < shortest:
                shortest = len(path)
                shortest_path = path
        return shortest_path

    def DFS(self, value1, lista_visitados=[]):
        if (value1 not in lista_visitados):
            lista_visitados.append(value1)

        datos = self.adjacency_list[value1]

        for i in datos:
            if (i not in lista_visitados):
                lista_visitados.append(i)
            
                self.DFS(i, lista_visitados)

        return lista_visitados


    def BFS(self, vertex, queue = [], visited = []):
        queue.append(vertex)
        while queue != []:
            nodo = queue.pop(0)
            if nodo not in visited:
                visited.append(nodo)
                for vecino in self.adj_list[nodo]:
                    if vecino not in visited:
                        queue.append(vecino)

        return visited
      
    def remove_same_input_output(self):
        output_counter = 0
        same_input_output = []
        keys = list(self.adjacency_list.keys())

        for key in keys:
            input_counter = 0
            output_counter = len(self.adjacency_list[key])
            for value in self.adjacency_list.values():
                if key in value:
                    input_counter += 1

            if input_counter == output_counter:
                same_input_output.append(key)
        if len(same_input_output) == 0:
            return False
        for vertex in same_input_output:
            self.remove_vertex(vertex)
            
      
        

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
customgraph.add_edge("D","F")
customgraph.add_edge("E","F")
customgraph.add_edge("F","E")

customgraph.print_graph()
#print(customgraph.recursive_paths_between_vertices("A", "E"))
#print(customgraph.find_paths("A", "E"))
#print(customgraph.find_shortest_path("A", "E"))
#print(customgraph.all_dfs_paths("C"))
# print(customgraph.all_bfs_paths("A"))
customgraph.remove_same_input_output()
print('---------------------')
customgraph.print_graph()