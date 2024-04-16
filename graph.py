class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                pass
        return False
    
    def remove_vertex(self,v):
        if v in self.adj_list.keys():
            for i in self.adj_list[v]:
               self.adj_list[i].remove(v)
            self.adj_list.pop(v) # or del self.adj_list[v]
            return True
        return False


        




graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_edge('A','B')
graph.add_edge('A','D')
graph.remove_edge('A','D')
graph.remove_vertex('A')
graph.add_edge('C','B')
graph.add_edge('C','D')
graph.add_vertex('E')
graph.remove_vertex('E')
graph.print_graph()