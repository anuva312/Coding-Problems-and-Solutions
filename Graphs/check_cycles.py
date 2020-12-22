# Check if cycles are present in a given graph

class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
        # To keep a list of nodes explored, to find cycles
        #  If coming back to the same node, a cycle is found
        self.in_path = {}
        self.ifcyclic = 0
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.visited[i] = 0
            self.adj_list[i] = []
            self.in_path[i] = 0

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a,b = map(int, input().split())
            self.adj_list[a].append(b)

    def explore(self,x):
        # Exploring the graph in depth first order
        self.visited[x] = 1
        self.in_path[x] = 1
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.explore(node)
            elif self.in_path[node]:
                self.ifcyclic = 1
        self.in_path[x] = 0

    def dfs(self):
        # Initializing no.of connected components to 0
        for node in self.adj_list.keys():
            if not self.visited[node]:
                self.explore(node)



if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    graph = Graph(n)
    graph.initialize_adj_list(m)
    (graph.dfs())
    print(graph.ifcyclic)

