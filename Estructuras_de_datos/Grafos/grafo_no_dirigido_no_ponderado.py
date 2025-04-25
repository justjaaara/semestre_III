'''
Implementación de grafo no dirigido no ponderado
'''

class Graph:

    def __init__(self) -> None:
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            

    
    def show_graph(self):
        for vertex in self.adjacency_list:
            print(f'{vertex} -> {self.adjacency_list[vertex]}')


#Prueba

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('C','D')
graph.add_edge('B','E')
graph.add_edge('D','E')

graph.add_edge('A','B')
print('Grafo original')
graph.show_graph()
print('\n')
graph.remove_vertex('A')
print('Después de remover A')
graph.show_graph()
