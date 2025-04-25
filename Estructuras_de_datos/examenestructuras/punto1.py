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

  def add_edge(self, v1, v2, directed=True):
    if v1 not in self.adj_list:
      self.add_vertex(v1)
    if v2 not in self.adj_list:
      self.add_vertex(v2)

    self.adj_list[v1].append(v2)
    if not directed:
      self.adj_list[v2].append(v1)

  def __str__(self):
    result = ""
    for vertex in self.adj_list:
      result += f"{vertex}: {', '.join(self.adj_list[vertex])}\n"
    return result

  def DFS(self, value1, lista_visitados=[]):
        if (value1 not in lista_visitados):
            lista_visitados.append(value1)

        datos = self.adj_list[value1]

        for i in datos:
            if (i not in lista_visitados):
                lista_visitados.append(i)

                self.DFS(i, lista_visitados)

        return lista_visitados
  
  def dfs(self, source_vertex):
        visited = set()
        custom_stack = stack()
        custom_stack.push(source_vertex)
        path = []

        while not custom_stack.is_empty():
            current_vertex = custom_stack.pop()
            path.append(current_vertex)
            if current_vertex not in visited:
                visited.add(current_vertex)

            for adjacent_vertex in self.adj_list[current_vertex]:
                if adjacent_vertex not in visited:
                    custom_stack.push(adjacent_vertex)

        return path

  def graph_can_reach(self, n):
        keys = list(self.adj_list.keys())
        source_vertex = keys[0]

        all_possible_paths = []

        source_vertex_value_list = list(self.adj_list[source_vertex])
        for value in source_vertex_value_list:
            path = self.dfs(value)
            all_possible_paths.append(path)
        print("All posible paths", all_possible_paths)
        for n_path in all_possible_paths:
            if len(n_path) >= n:
                return n_path

        return []


graph = ALGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")
graph.add_vertex("H")
graph.add_vertex("I")
graph.add_vertex("J")
graph.add_vertex("K")

graph.add_edge("A", "B", directed=True)
graph.add_edge("A","C", directed=True)
graph.add_edge("A","D", directed=True)
graph.add_edge("A","E", directed=True)
graph.add_edge("A","F", directed=True)

graph.add_edge("B","G", directed=True)
graph.add_edge("B","H", directed=True)

graph.add_edge("D", "I", directed=True)
graph.add_edge("D", "J", directed=True)

graph.add_edge("F","K", directed=True)

print(graph)
print("EL grafo puede alcanzar 3 saltos")
print(graph.graph_can_reach(3))

