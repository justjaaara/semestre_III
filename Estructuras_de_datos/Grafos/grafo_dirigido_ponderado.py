'''
Implementación de grafo dirigido ponderado

'''


class Graph:

  def __init__(self):
    self.adjacency_list = {}

  def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = {}
      return True
    return False

  def add_edge(self, source_vertex, destination_vertex, weigth):
    if source_vertex in self.adjacency_list and destination_vertex in self.adjacency_list:
      self.adjacency_list[source_vertex][destination_vertex] = weigth
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
        print(other_vertex)
      del self.adjacency_list[vertex]
      return True
    return False


  def print_graph(self):
    for vertex in self.adjacency_list:
      print(vertex, " : ", self.adjacency_list[vertex])



customGraph = Graph()
customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")
customGraph.add_vertex("E")
customGraph.add_edge("A","B",5)
customGraph.add_edge("A","C",10)
customGraph.add_edge("B","A",5)
customGraph.add_edge("C","D",4)
customGraph.add_edge("B","E",3)
customGraph.add_edge("D","E",10)
customGraph.add_edge("E","B",3)


customGraph.print_graph()
print("\n")
#print("Despues de remover A")
#customGraph.remove_vertex("A")
#customGraph.print_graph()