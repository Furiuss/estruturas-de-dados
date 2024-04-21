class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2) -> bool:
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2) -> bool:
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
        return False
    
    def remove_vertex(self, vertex) -> bool:
        if vertex in self.adj_list.keys():
            for _ in (self.adj_list[vertex]):
                self.adj_list[_].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
            
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('B', 'C')
my_graph.remove_vertex('A')
# print(my_graph.remove_edge('A', 'B'))
# print(my_graph.remove_edge('A', 'C'))


my_graph.print_graph()