'''
Implementación de grafo dirigido no ponderado
'''

class Graph:

    def __init__(self) -> None:
        self.adjacency_list = {}

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

    def remove_edge(self, source_vertex, destination_vertex):
        if source_vertex in self.adjacency_list and destination_vertex in self.adjacency_list:
            self.adjacency_list[source_vertex].remove(destination_vertex)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list:
                if vertex in self.adjacency_list[other_vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

            

    
    def show_graph(self):
        for vertex in self.adjacency_list:
            print(f'{vertex} -> {self.adjacency_list[vertex]}')


#Prueba

customGraph = Graph()
customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")
customGraph.add_edge("A","B")
customGraph.add_edge("A","C")
customGraph.add_edge("B","A")
customGraph.add_edge("C","D")
customGraph.add_edge("B","E")
customGraph.add_edge("D","E")
customGraph.add_edge("E","B")


customGraph.show_graph()
print("\n")
print("Despues de remover A")
customGraph.remove_vertex("A")
customGraph.show_graph()