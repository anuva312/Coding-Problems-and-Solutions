# Check if cycles are present in a given graph

class Graph:
    def __init__(self,n):
        self.adj_list = {}
        self.visited = {}
        self.in_path = {}
        self.ifcyclic = 0
        # self.rev_adj_list = {}
        # self.clock = 0
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.visited[i] = 0
            self.adj_list[i] = []
            self.in_path[i] = 0
        # self.post = {}
        # self.prev = {}
        # self.max_post = 0

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a,b = map(int, input().split())
            # self.rev_adj_list[b].append(a)
            self.adj_list[a].append(b)

    def explore(self,x):
        # Exploring the graph in depth first order
        # self.prev[x] = self.clock
        # self.clock+=1
        self.visited[x] = 1
        self.in_path[x] = 1
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.explore(node)
            elif self.in_path[node]:
                self.ifcyclic = 1
        self.in_path[x] = 0
        # self.post[x]= self.clock
        # self.clock+=1

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

