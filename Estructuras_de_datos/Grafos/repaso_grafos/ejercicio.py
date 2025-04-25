class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, source, destination, weight):
        if source in self.adjacency_list and destination in self.adjacency_list:
            self.adjacency_list[source][destination] = weight
            return True
        return False

    def remove_edge(self, source, destination):
        if source in self.adjacency_list and destination in self.adjacency_list[source]:
            del self.adjacency_list[source][destination]
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for vertices in self.adjacency_list.values():
                if vertex in vertices:
                    del vertices[vertex]
            return True
        return False

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        for adjacent in self.adjacency_list[vertex]:
            if not visited[adjacent]:
                self.topological_sort_util(adjacent, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = {key: False for key in self.adjacency_list}
        stack = []
        for vertex in self.adjacency_list:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
        return stack

    def longest_path(self, source_vertex):
        stack = self.topological_sort()
        distances = {vertex: float('-inf') for vertex in self.adjacency_list}
        distances[source_vertex] = 0

        while stack:
            vertex = stack.pop(0)
            if distances[vertex] != float('-inf'):
                for adjacent, weight in self.adjacency_list[vertex].items():
                    if distances[adjacent] < distances[vertex] + weight:
                        distances[adjacent] = distances[vertex] + weight

        return distances

# Creación del grafo y adición de vértices y aristas
customGraph = Graph()
customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")
customGraph.add_edge("A","B", 10)
customGraph.add_edge("A","C", 5)
customGraph.add_edge("B","E", 20)
customGraph.add_edge("C","D", 2)
customGraph.add_edge("C","A", 5)
customGraph.add_edge("D","E", 4)
customGraph.add_edge("E","B", 20)

customGraph.print_graph()
print("\n")

# Ejecución del método para encontrar la ruta más larga desde "A"
longest_paths_from_A = customGraph.longest_path("A")
print(f"Las rutas más largas desde A son: {longest_paths_from_A}")
