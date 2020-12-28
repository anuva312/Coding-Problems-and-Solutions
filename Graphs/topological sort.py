# Find the topological list ordering of the graph

class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
        self.topological_list = []
        self.size = n + 1
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.visited[i] = 0
            self.adj_list[i] = []

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a,b = map(int, input().split())
            self.adj_list[a].append(b)

    def explore(self,x):
        # Exploring the graph in depth first order
        self.visited[x] = 1
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.explore(node)
        # Adding the node to the topological sort list
        self.topological_list.append(x)

    def dfs(self):
        for node in range(1,self.size):
            if not self.visited[node]:
                self.explore(node)


        


if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    graph = Graph(n)
    graph.initialize_adj_list(m)
    (graph.dfs())
    print(*graph.topological_list[::-1])

