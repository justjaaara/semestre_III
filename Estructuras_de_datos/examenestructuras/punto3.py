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
class ALGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, label):
        if label not in self.adj_list:
            self.adj_list[label] = []

    def add_edge(self, source_vertex, destination_vertex):
        if source_vertex in self.adj_list and destination_vertex in self.adj_list:
            self.adj_list[source_vertex].append(destination_vertex)
            return True
        return False

    def __str__(self):
        result = ""
        for vertex in self.adj_list:
            result += f"{vertex}: {', '.join(self.adj_list[vertex])}\n"
        return result


    def find_paths(self, source_vertex, destination_vertex):
        paths = []
        custom_stack = stack()
        custom_stack.push(source_vertex)
        path = []
        visited = set()

        while not custom_stack.is_empty():
            current_vertex = custom_stack.pop()
            if current_vertex == destination_vertex:
                path.append(current_vertex)
                paths.append(list(path))
                path.pop()
                visited.remove(current_vertex)
            else:
                path.append(current_vertex)
                for adjacency_vertex in self.adj_list[current_vertex]:
                    if adjacency_vertex not in visited:
                        custom_stack.push(adjacency_vertex)
                        visited.add(adjacency_vertex)
        return paths

    def find_paths_excluding_vertices(self, source_vertex, destination_vertex, excluded_vertices):
        all_possible_paths = self.find_paths(source_vertex, destination_vertex)
        valid_paths = []

        for path in all_possible_paths:
            exclude = False
            for excluded_vertex in excluded_vertices:
                if excluded_vertex in path:
                    exclude = True
                    break
            if not exclude:
                valid_paths.append(path)
        print(all_possible_paths)
        print(valid_paths)
        if len(valid_paths) > 0:
            return len(valid_paths)
        else:
            return 0


customgraph = ALGraph()

customgraph.add_vertex("A")
customgraph.add_vertex("B")
customgraph.add_vertex("C")
customgraph.add_vertex("D")
customgraph.add_vertex("E")
customgraph.add_vertex("F")
customgraph.add_vertex("G")
customgraph.add_vertex("H")
customgraph.add_vertex("I")

customgraph.add_edge("A", "C")
customgraph.add_edge("C", "G")
customgraph.add_edge("C", "E")
customgraph.add_edge("C", "D")
customgraph.add_edge("D", "B")
customgraph.add_edge("E", "H")
customgraph.add_edge("E", "D")
customgraph.add_edge("F", "G")
customgraph.add_edge("G", "H")
customgraph.add_edge("H", "I")
customgraph.add_edge("I", "D")

print(customgraph)

print(customgraph.find_paths_excluding_vertices("A", "D", ["E", "F"]))

