# Find the number of strongly connected components in the graph
import sys
sys.setrecursionlimit(10**6) 

class Graph:
    def __init__(self, n):
        self.adj_list = {}
        self.visited = {}
        self.rev_adj_list = {}
        self.post_time = []
        self.size = n + 1
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1, n + 1):
            self.visited[i] = 0
            self.adj_list[i] = []
            self.rev_adj_list[i] = []

    def initialize_adj_list(self, m):
        # Filling the adjacency list
        for _ in range(m):
            a, b = map(int, input().split())
            self.rev_adj_list[b].append(a)
            self.adj_list[a].append(b)

    def explore(self, x):
        # Exploring the graph in depth first order
        self.visited[x] = 1
        for node in self.adj_list[x]:
            if not self.visited[node]:
                self.explore(node)
        self.post_time.append(x)

    def dfs(self):
        # Initializing no.of connected components to 0
        for node in range(1, self.size):
            if not self.visited[node]:
                self.explore(node)

    def find_scc(self):
        scc = 0
        stack = self.post_time
        self.post_time = []
        self.adj_list = self.rev_adj_list
        for i in range(1, self.size):
            self.visited[i] = 0
        while stack:
            node = stack.pop()
            if not self.visited[node]:
                self.explore(node)
                scc += 1
        return scc


if __name__ == '__main__':
    # Taking input : no.of vertices, edges
    n, m = map(int, input().split())
    graph = Graph(n)
    graph.initialize_adj_list(m)
    graph.dfs()
    print(graph.find_scc())
